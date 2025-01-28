# Generated by Django 5.1.4 on 2025-01-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_carousel_carouselimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="RestrictedPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                ("content", models.TextField(verbose_name="Content")),
                (
                    "access_code",
                    models.CharField(max_length=20, verbose_name="Access Code"),
                ),
            ],
            options={
                "verbose_name": "Restricted Page",
                "verbose_name_plural": "Restricted Pages",
            },
        ),
    ]
