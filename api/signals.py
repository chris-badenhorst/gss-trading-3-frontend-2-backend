from django.db.models.signals import pre_save
from .models import Custom_User
from django.dispatch import receiver


def updateUser(sender, instance, **kwargs):
    if instance.email != "":
        instance.username = instance.email
    
pre_save.connect(updateUser, sender=Custom_User)