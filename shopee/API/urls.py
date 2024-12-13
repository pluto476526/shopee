from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, LoginAPIView


# router = DefaultRouter()

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='api-login'),
]
