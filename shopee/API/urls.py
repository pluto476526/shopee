from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, LoginAPIView, InventoryListAPIView, ProductDetailAPIView, ProductCreateAPIView, LogOutAPIView


# router = DefaultRouter()

urlpatterns = [
    path('', InventoryListAPIView.as_view(), name='api-home'),
    path('register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='api-login'),
    path('inventory/', InventoryListAPIView.as_view(), name='api-inventory'),
    path('inventory/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product_details'),
    path('inventory/create/', ProductCreateAPIView.as_view(), name='api-product_create'),
    path('logout/', LogOutAPIView.as_view(), name='api=logout'),
]
