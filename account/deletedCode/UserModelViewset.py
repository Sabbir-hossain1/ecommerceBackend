from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from account.models import User
from account.serializers import UserRegistrationSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }


# Create your views here.
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request,*args, **kwargs):        
        data = request.data               
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()          
            token = get_token_for_user(user)
            return Response({"token":token, 'msg':'Registration successful'}, status=status.HTTP_201_CREATED)           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():            
            email = serializer.data['email']
            password = serializer.data['password']  
            print(email, password)         
            user = authenticate(email=email, password=password)
            print("authenticated user: ", user)

            if user is not None:
                token = get_token_for_user(user)
                return Response(
                    {'token':token, 
                     'msg':'Login Successful',
                     'fullName': user.fullName,
                     "email":user.email,                     
                     },
                      status=status.HTTP_200_OK)
            else:
                return Response({"errors":{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckEmailExistsView(APIView):
    def post(self, request, *args, **kwargs):         
        email = request.data.get('email', None)
        if email:
            user_exists  = User.objects.filter(email=email).exists()
            if user_exists:
                return Response({"emailExist":True})
            else:
                return Response({"emailExist":False}) 

