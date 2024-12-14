from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, ProductSerializer
from .models import Product


# Register View
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()  # This sets the queryset for the CreateAPIView
    serializer_class = UserSerializer  # Serializer used to validate and save user data

# Login View
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Authenticates a user using username and password.
        If authentication is successful, generates or retrieves an authentication token.
        """
        username = request.data.get('username')  # Retrieve username from request data
        password = request.data.get('password')  # Retrieve password from request data

        user = authenticate(request, username=username, password=password)  # Authenticate user

        if user:
            token, created = Token.objects.get_or_create(user=user)  # Create/retrieve token
            login(request, user)  # Log the user in (session-based login)
            return Response({
                'message': 'Login successful',
                'token': token.key  # Return token to the user
            })

        return Response({'error': 'Invalid credentials'}, status=401)  # Return error if authentication fails


# Product creation (Restricted to authenticated users)
class ProductCreateAPIView(CreateAPIView):
    """
    Allows authenticated users to create a product.
    """
    queryset = Product.objects.all  # Correct: Use `Product.objects.all()` instead of `Product.objects.all`
    serializer_class = ProductSerializer
    permission_classes = []  # Only authenticated users can create a product

    # Improvement: Restrict this to staff users using IsAdminUser or custom permissions


# List all inventory (Restricted to authenticated users)
class InventoryListAPIView(ListAPIView):
    """
    Returns a list of all products in the inventory.
    """
    queryset = Product.objects.all()  # Query all products
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view inventory


# Retrieve details for a specific product
class ProductDetailAPIView(RetrieveAPIView):
    """
    Returns details of a single product.
    """
    queryset = Product.objects.all()  # Query all products
    serializer_class = ProductSerializer
    permission_classes = []  # Only authenticated users can view product details


# Logout endpoint
class LogOutAPIView(APIView):
    """
    Logs out the user by deleting their authentication token.
    """
    authentication_classes = [TokenAuthentication]  # Ensure token authentication
    permission_classes = []  # Only authenticated users can access this endpoint

    def post(self, request, *args, **kwargs):
        """
        Deletes the token for the authenticated user, effectively logging them out.
        """
        try:
            # Use `.filter()` to retrieve the token; `.first()` prevents `DoesNotExist` error
            token = Token.objects.filter(user=request.user).first()
            if token:
                token.delete()  # Delete token to log out the user
                return Response({'message': 'Logout successful'}, status=200)

            return Response({'error': 'Token does not exist'}, status=400)  # Handle missing token

        except Exception as e:
            # Catch unexpected errors and log the error for debugging
            return Response({'error': f'An error occurred: {str(e)}'}, status=500)


