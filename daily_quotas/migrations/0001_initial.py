# Generated by Django 4.1.5 on 2023-01-12 03:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailyQuota",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("daily", "Daily"), ("total", "Default")],
                        default="total",
                        max_length=32,
                    ),
                ),
                ("work", models.FloatField(default=0)),
                ("sleep", models.FloatField(default=0)),
                ("study", models.FloatField(default=0)),
                ("hobby", models.FloatField(default=0)),
                ("health", models.FloatField(default=0)),
            ],
        ),
    ]
