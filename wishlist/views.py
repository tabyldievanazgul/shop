from rest_framework import generics
from rest_framework.generics import ListAPIView

from wishlist.models import WishList
from wishlist.serializers import WishlistAddSerializer


class WishlistAddApiView(generics.CreateAPIView):
    queryset = WishList
    serializer_class = WishlistAddSerializer

# class WishlistApiView(generics.ListAPIView):
#     queryset = WishList
#     serializer_class = WishListSerializer