from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions 

from profiles.serializers import RegisterSerializer, UserSerializer

# Create your views here.

# kullanıcıların kayıt olurken istek yapacağı view
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
