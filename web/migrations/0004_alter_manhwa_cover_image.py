# Generated by Django 3.2.5 on 2021-07-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_alter_manhwa_cover_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manhwa",
            name="cover_image",
            field=models.ImageField(upload_to="images/cover_images"),
        ),
    ]
