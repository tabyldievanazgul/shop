from rest_framework import generics, permissions
from django.shortcuts import render
from  .models import Product
from .serializers import ProductSerializer
class ProductListApiView(generics.ListCreateAPIView):
    permissions = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
