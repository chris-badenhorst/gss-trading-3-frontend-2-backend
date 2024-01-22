from django.db import models

# Create your models here.
class SurveyItem(models.Model):
    assessment_date = models.DateField(auto_now_add=True, null=True, blank=True)
    responsible_employee = models.CharField(max_length=20, null=True, blank=True)
    survey_number = models.CharField(max_length=8, null=True, blank=True)
    present_on_site = models.TextField(null=True, blank=True)
    premisis_occupaid_vacant = models.CharField(max_length=10, null=True, blank=True)
    survey_items = models.JSONField(blank=True, null=True)
    other_items = models.JSONField(blank=True, null=True)
    comment = models.TextField(null=True, blank=True)
    