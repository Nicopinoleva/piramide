# Generated by Django 3.1.1 on 2020-09-27 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piramide', '0008_card_decknum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='color',
        ),
    ]