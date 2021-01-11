from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Page


from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    hero_titel = models.CharField(
        max_length=140,
        blank=False,
        help_text="Überschrift erster Abschnitt",
    )

    hero_text = models.TextField(
        max_length=500,
        blank=False,
        help_text="Text neben/unter dem Banner",
    )

    banner_hintergrund_bild = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text="Banner Hintergrundbild",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_titel"),
        FieldPanel("hero_text"),
        ImageChooserPanel("banner_hintergrund_bild"),

    ]
