from rest_framework import serializers
from .models import Product, ImageProduct

class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('image',)
        model = ImageProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('category',  'name', 'parent')
        fields = ('id', 'category', 'name', 'slug', 'description',
                  'price', 'stock', 'available', 'created', 'updated',)
        model = Product

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        # print(representation)
        if instance.images.exists():
            representation['image'] = ImageProductSerializer(
                instance.images.all(), many=True).data
        return representation



