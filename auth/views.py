from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


class SignUp(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=username, email=email, password=make_password(password))
        user.save()

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

class SignIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        })
