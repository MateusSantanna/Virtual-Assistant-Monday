# Generated by Django 4.1.5 on 2023-01-12 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="academic_infos",
        ),
        migrations.RemoveField(
            model_name="user",
            name="daily_quotas",
        ),
        migrations.RemoveField(
            model_name="user",
            name="finance_infos",
        ),
        migrations.RemoveField(
            model_name="user",
            name="health_infos",
        ),
    ]
