# Generated by Django 3.2.5 on 2021-08-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0006_alter_manhwa_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manhwa",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
