# from wagtail.core.models import Page
# from wagtail.core.fields import StreamField
# from wagtail.admin.edit_handlers import StreamFieldPanel
# from wagtail.snippets.blocks import SnippetChooserBlock
# from streams import blocks


# class FlexibleSeite(Page):

#     body = StreamField([
#         ("titel", blocks.TitelBlock()),
#         ("cards", blocks.CardsBlock()),
#         ("tabellen_block", blocks.TabellenBlock()),
#     ], null=True, blank=True)

#     content_panels = Page.content_panels + [
#         StreamField("body"),
#     ]

#     class Meta:
#         verbose_name = "variablen Aufbau"
