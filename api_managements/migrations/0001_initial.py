# Generated by Django 4.1.5 on 2023-01-09 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("schedules", "0001_initial"),
        ("daily_quotas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="APIManagement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("auto_schedule", models.BooleanField(default=False)),
                (
                    "active_time",
                    models.DecimalField(decimal_places=2, max_digits=3, null=True),
                ),
                (
                    "daily_quotas",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="daily_quotas.dailyquota",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="management",
                        to="schedules.schedule",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
