# Generated by Django 4.2.3 on 2023-08-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carSelling", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Registered",
            new_name="Registration",
        ),
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]