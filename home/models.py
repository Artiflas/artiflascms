from django.db import models
from django.core.exceptions import ValidationError
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core import blocks as wagtail_blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks


class SeiteMitHeroBanner(Page):
    class Meta:
        verbose_name = "Hero Banner"

    template = "home/hero_banner_seite.html"
    hero_titel = models.CharField(
        max_length=140,
        blank=True,
        help_text="Überschrift erster Abschnitt",
    )

    hero_text = models.TextField(
        max_length=500,
        blank=True,
        help_text="Text neben/unter dem Banner. Maximal 500 Zeichen.",
    )

    banner_hintergrund_bild = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        help_text="Banner Hintergrundbild",
        on_delete=models.SET_NULL,
    )
    bild_link_intern = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Interner Link für das Hintergrundbild hinterlegen',
        on_delete=models.SET_NULL,

    )
    bild_link_extern = models.URLField(
        blank=True,
        help_text='Verlinkung zu einer externen Seite',
    )

    body = StreamField([
        ("titel", blocks.TitelBlock()),
        ("cards", blocks.CardsBlock()),
        ("tabellen_block", blocks.TabellenBlock()),
        ("richtext_with_title", blocks.RichTextMitTitelBlock()),
        # ("richtext", wagtail_blocks.RichTextBlock(
        #     template="streams/simple_richtext_block.html",
        #     # features=["bold", "italic", "ol", "ul", "link"]
        # )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_titel"),
        FieldPanel("hero_text"),
        ImageChooserPanel("banner_hintergrund_bild"),
        PageChooserPanel("bild_link_intern"),
        FieldPanel("bild_link_extern"),
        StreamFieldPanel("body"),
    ]

    def clean(self):
        super().clean()

        if self.bild_link_intern and self.bild_link_extern:

            raise ValidationError({
                'bild_link_intern': ValidationError("Bitte entweder eine interne Seite auswählen oder nur einen externen Link hinterlegen!"),
                'bild_link_extern': ValidationError("Bitte entweder eine interne Seite auswählen oder nur einen externen Link hinterlegen!"),
            })
