# Generated by Django 5.0.2 on 2024-02-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messaging_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="has_been_read",
            field=models.BooleanField(default=False),
        ),
    ]
