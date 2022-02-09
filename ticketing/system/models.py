from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Department(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)


class UserProfile(models.Model):  
    user = models.OneToOneField(User) 
    mobile = models.CharField(max_length=11) #for example 09123456789
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)


class Ticket(models.Model):
    subject = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    operator = models.ForeignKey(User, null=True)
    is_answered = models.BooleanField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)



class File(models.Model):
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=100)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)


class Answer(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)

