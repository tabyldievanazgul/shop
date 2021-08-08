from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer
from .models import WishList, WishlistProduct


class WishlistAddSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    product_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        fields = ('id', 'products', 'product_id')
        model = WishList

    def create(self, validated_data):
        request = self.context.get('request')
        product_id = validated_data.pop('product_id')
        product_obj = Product.objects.get(id=product_id)
        wishlist = WishList.objects.get(user=request.user)
        if wishlist:
            WishlistProduct.objects.create(
                wishlist=wishlist, product=product_obj
            )
        return WishList.objects.filter(user=request.user)

#
# class WishListProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = "__all__"
#         model = WishlistProduct
#
#
# class WishListSerializer(serializers.ModelSerializer):
#     class Meta:
#         # fields = ('category',  'name', 'parent')
#         fields = "__all__"
#         model = WishList
#
#     def to_representation(self, instance):
#         representation = super(WishListSerializer, self).to_representation(instance)
#         # print(representation)
#         if instance.wishlists.exists():
#             representation['wishlists'] = WishlistAddSerializer(
#                 instance.images.all(), many=True).data
#         if instance.products.exists():
#             representation['products'] = WishlistAddSerializer(
#                 instance.products.all(), many=True).data
#         return representation
#
#
