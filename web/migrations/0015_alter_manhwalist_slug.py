# Generated by Django 3.2.6 on 2021-12-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0014_manhwa_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manhwalist",
            name="slug",
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
