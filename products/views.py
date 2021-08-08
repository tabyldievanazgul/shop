from rest_framework import generics, permissions
from django.shortcuts import render
from  .models import Product, ImageProduct
from .serializers import ProductSerializer, ImageProductSerializer
from rest_framework.pagination import  PageNumberPagination
from rest_framework import filters


class MyPaginationClass(PageNumberPagination):
    page_size = 2

    # def get_paginated_response(self, data):
    #     for i in range(self.page_size):
    #         description = data[i]['description']
    #         if len(description) > 20:
    #             data[i]['description']  = description[:20] + '...'
    #         return super().get_paginated_response(data=data)


class ProductListApiView(generics.ListCreateAPIView):
    permissions = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPaginationClass
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    def get_queryset(self):
        price = self.request.query_params.get('price')
        # print(price)
        queryset = super().get_queryset()
        if price:
            price_from, price_to = price.split('-')
            queryset = queryset.filter(price__gt=price_from, price__lt=price_to)
        return queryset


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageListApiView(generics.ListCreateAPIView):
    # permissions = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ImageProduct.objects.all()
    serializer_class = ImageProductSerializer