from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class TitelBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required=True,


    )

    class Meta:
        template = "streams/titel_block.html"
        icon = "edit"
        label = "Titel"
        help_text = "Erzeugt eine Überschrift, um einen neuen Abschnitt einzuleiten"


class CardsBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("titel", blocks.CharBlock(max_length=100,
                                           help_text="Fett formatierter Text. Maximale Länge 100 Zeichen")),
                ("text", blocks.TextBlock(max_length=255,
                                          help_text="Optionaler Text. Maximale Länge 255 Zeichen", required=False)),
                ("image", ImageChooserBlock(
                    help_text="Bild in der Größe 906px x 588px")),
            ]
        )
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Karte mit Bild"


class TabellenBlock(TableBlock):
    """Tabelle"""
    class Meta:
        template = "streams/tabellen_block.html"
        label = "Tabelle"
        icon = "table"
        help_text = "Tabellen Zeilen und Spalten können entfernt und hinzugefügt werden"


class RichTextMitTitelBlock(blocks.StructBlock):

    titel = blocks.CharBlock(max_length=50)
    context = blocks.RichTextBlock()

    # class Meta:
    #     template = "simple_richtext_block.html"


# class BildUndTextBlock(blocks.StructBlock):

#     image = ImageChooserBlock(help_text="Bild in der Größe 906px x 588px")
