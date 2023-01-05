# Generated by Django 4.1.5 on 2023-01-05 19:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Heath_Info",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("height", models.DecimalField(decimal_places=2, max_digits=3)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=8)),
                ("bmi", models.DecimalField(decimal_places=2, max_digits=4)),
                ("ideal_weight", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
