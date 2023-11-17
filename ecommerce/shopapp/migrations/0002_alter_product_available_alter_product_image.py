# Generated by Django 4.1 on 2023-10-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="product"),
        ),
    ]
