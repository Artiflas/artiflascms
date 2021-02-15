# Generated by Django 3.1.5 on 2021-02-15 07:42

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210215_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seitemitherobanner',
            name='body',
            field=wagtail.core.fields.StreamField([('titel', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('titel', wagtail.core.blocks.CharBlock(help_text='Fett formatierter Text. Maximale Länge 100 Zeichen', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optionaler Text. Maximale Länge 255 Zeichen', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Bild in der Größe 906px x 588px'))])))])), ('tabellen_block', streams.blocks.TabellenBlock()), ('richtext_with_title', wagtail.core.blocks.StructBlock([('titel', wagtail.core.blocks.CharBlock(max_length=50)), ('context', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]