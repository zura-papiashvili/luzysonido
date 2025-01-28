# Generated by Django 5.1.4 on 2025-01-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_restrictedpage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="restrictedpage",
            options={
                "verbose_name": "Página para iniciados",
                "verbose_name_plural": "Páginas para iniciados",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="access_type",
            field=models.CharField(
                choices=[("public", "Público"), ("private", "Privado")],
                default="public",
                max_length=20,
                verbose_name="tipo de acceso",
            ),
        ),
        migrations.AlterField(
            model_name="restrictedpage",
            name="access_code",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="codigo de acceso"
            ),
        ),
        migrations.AlterField(
            model_name="restrictedpage",
            name="content",
            field=models.TextField(verbose_name="contenido"),
        ),
        migrations.AlterField(
            model_name="restrictedpage",
            name="title",
            field=models.CharField(max_length=100, verbose_name="título"),
        ),
    ]
