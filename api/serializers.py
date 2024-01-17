from rest_framework import serializers
from .models import SurveyItem
import json

class SurveyItemSerializer(serializers.ModelSerializer):   
    

# Assuming your survey_items string is stored in a variable
    class Meta:
         model = SurveyItem
         fields = '__all__'
        