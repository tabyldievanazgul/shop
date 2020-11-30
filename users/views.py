from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView, View
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .send_mail import send_email
User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                #todo add send message with celery
                send_email(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)



class ActivationView(View):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return render(request, 'accounts/index.html', {})
        except User.DoesNotExist:
            return render(request, 'accounts/link_exp.html', {})

class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer

