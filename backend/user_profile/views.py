from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate

@api_view(['POST'])
def UserLogin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if hasattr(user, 'profile') and user.profile.is_head:
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token), 'is_head': True}, status=status.HTTP_200_OK)
        else:
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token), 'is_head': False}, status=status.HTTP_200_OK)
    else:
        raise AuthenticationFailed('Incorrect credentials')
