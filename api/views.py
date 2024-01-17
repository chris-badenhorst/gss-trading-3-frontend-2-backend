from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SurveyItem
from .serializers import SurveyItemSerializer
import json


# Create your views here.
@api_view(["POST"])
def addSurveys(request):
    data = request.data
    
    survey_item = SurveyItem.objects.create(
        responsible_employee=data["responsibleEmployee"],
        present_on_site=data["presentOnSite"],
        premisis_occupaid_vacant=data["premisesOccupiedOrVacant"],
        survey_items=data["surveyItems"],
        comment=data["comment"],
    )
    serializer = SurveyItemSerializer(survey_item)

    return Response(serializer.data)


@api_view(["GET"])
def getSurveys(request):
    survey_items = SurveyItem.objects.all()
    serializer = SurveyItemSerializer(survey_items, many=True)  

    return Response(serializer.data)
