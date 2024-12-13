from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer


# Register View
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Login View
class LoginAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, *args, **kwargs):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate User
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login succesful'})

        return Response({'error': 'Invalid credentials'}, status=401)

    def get(self, request, *args, **kwargs):
        return Response({'error': 'Get method not allowed'}, status=405)
        
