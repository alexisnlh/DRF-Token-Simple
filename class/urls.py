from django.urls import path
from .views import RegisterUserAPIView, LoginUserAPIView, ProfileUserAPIView


urlpatterns = [
    path('register', RegisterUserAPIView.as_view()),
    path('login', LoginUserAPIView.as_view()),
    path('profile', ProfileUserAPIView.as_view())
]
