# Generated by Django 3.1.5 on 2021-02-14 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210214_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='test_text',
        ),
    ]
