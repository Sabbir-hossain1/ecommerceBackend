
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer,UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access': str(refresh.access_token)
    }

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
    
class CheckEmailExistsView(APIView):
    def post(self, request, *args, **kwargs):         
        email = request.data.get('email', None)
        if email:
            user_exists  = User.objects.filter(email=email).exists()
            if user_exists:
                return Response({"emailExist":True})
            else:
                return Response({"emailExist":False}) 
    

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_token_for_user(user)
            return Response({'token':token,'name':user.fullName, 'msg':'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)