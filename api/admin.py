from django.contrib import admin
from .models import SurveyItem, Custom_User

# Register your models here.
admin.site.register(SurveyItem)
admin.site.register(Custom_User)