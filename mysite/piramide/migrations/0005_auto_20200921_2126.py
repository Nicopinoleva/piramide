# Generated by Django 3.1.1 on 2020-09-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piramide', '0004_auto_20200920_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
