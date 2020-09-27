# Generated by Django 3.1.1 on 2020-09-27 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piramide', '0009_remove_card_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='piramide.player'),
        ),
    ]
