from django.urls import path
from account.views import UserRegistrationView, CheckEmailExistsView,UserLoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('email-availability/', CheckEmailExistsView.as_view(), name='check-email'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

