from rest_framework import generics, permissions
from django.shortcuts import render
from .models import Category
# from .permissions import IsAuthorOrReadOnly
from .serializers import CategorySerializer
from django.contrib.auth import get_user_model
from products.views import MyPaginationClass

User = get_user_model()
# Create your views here.
class CategoryListApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPaginationClass

class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer












