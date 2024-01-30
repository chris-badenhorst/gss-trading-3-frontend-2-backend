from rest_framework import serializers
from .models import SurveyItem, Custom_User
from django.contrib.auth.hashers import make_password

class SurveyItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = SurveyItem
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Custom_User
        fields = ["id", "name", "email", "password", "quote", "survey", "is_staff"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
