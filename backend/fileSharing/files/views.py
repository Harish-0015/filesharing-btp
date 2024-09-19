
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from files.models import User

from files.serializer import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class GetUserDetailsView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get(self, request, unique_id):
        try:
            # Fetch the user by the unique_id
            user = User.objects.get(unique_id=unique_id)
        except User.DoesNotExist:
            raise NotFound(detail="User not found")
        
        # Serialize the user data
        serializer = self.get_serializer(user)
        
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_role(request):
    user_role = request.user.role
    return Response({'role': user_role}, status=status.HTTP_200_OK)

# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

