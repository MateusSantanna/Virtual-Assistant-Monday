# Generated by Django 4.1.5 on 2023-01-12 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("health_infos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="healthinfo",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="health_infos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
