from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import SurveyItem, Custom_User
from .serializers import SurveyItemSerializer, UserSerializer
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .permissions import CanAccessSurveys, CanAddSurveys, canRegisterUser
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated,CanAddSurveys])
def addSurveys(request):
    data = request.data
    
    survey_item = SurveyItem.objects.create(
        responsible_employee=data["responsibleEmployee"],
        survey_number=data["surveyNumber"],
        present_on_site=data["presentOnSite"],
        premisis_occupaid_vacant=data["premisesOccupiedOrVacant"],
        survey_items=data["surveyItems"],
        other_items=data["other"],
        comment=data["comment"],
    )
    serializer = SurveyItemSerializer(survey_item)

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated, CanAccessSurveys])
def getSurveys(request):
    survey_items = SurveyItem.objects.all()
    serializer = SurveyItemSerializer(survey_items, many=True)  

    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, CanAccessSurveys])
def delete_survey(request, pk):
    try:
        survey_item = SurveyItem.objects.get(id=pk)
        survey_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except SurveyItem.DoesNotExist:
        return Response({"error": "SurveyItem not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(["POST"])
@permission_classes([canRegisterUser])
def register_user(request):
    # Assuming UserSerializer is your serializer for the User model
    serializer = UserSerializer(data=request.data)  # Pass request.data to provide data to the serializer
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # After saving the user, retrieve the user object from the database
    user_obj = Custom_User.objects.get(email=request.data['email'])

    # Generate tokens for the use
    # Return the tokens in the response
    return Response({"message": "success"},status=status.HTTP_201_CREATED)
    
@api_view(["POST"])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = Custom_User.objects.filter(email=email).first()
    if not user:
        return Response({"error": "User not found"})
    if not user.check_password(password):
        return Response({"error": "Incorrect password"})
    
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)

    return Response({"refresh": str(refresh), "access": str(access)}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_user(request, pk):
    user = Custom_User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
        
