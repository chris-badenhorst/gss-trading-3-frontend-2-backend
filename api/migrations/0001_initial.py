# Generated by Django 5.0.1 on 2024-01-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="surveyItem",
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
                ("assessment_date", models.DateField(blank=True, null=True)),
                (
                    "responsible_employee",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("present_on_site", models.TextField(blank=True, null=True)),
                (
                    "premisis_occupaid_vacant",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                ("survey_items", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
