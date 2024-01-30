from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Custom_User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    quote = models.BooleanField(default=False)
    survey = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def get_username(self):
        return self.email  # Corrected indentation
