# Generated by Django 5.0.1 on 2024-01-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_surveyitem_other_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyitem",
            name="survey_number",
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]