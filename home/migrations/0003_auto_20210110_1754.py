# Generated by Django 3.1.5 on 2021-01-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_hintergrund_bild',
            field=models.ForeignKey(blank=True, help_text='Banner Hintergrundbild', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.TextField(blank=True, help_text='Text neben/unter dem Banner', max_length=500),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_titel',
            field=models.CharField(blank=True, help_text='Überschrift erster Abschnitt', max_length=140),
        ),
    ]