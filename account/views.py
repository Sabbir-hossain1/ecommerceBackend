from django.shortcuts import render
from rest_framework import viewsets
from account.models import User
from account.serializers import UserRegistrationSerializer


# Create your views here.
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer