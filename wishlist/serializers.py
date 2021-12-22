from typing import NoReturn
from rest_framework import serializers

from wishlist.models import Wishlist
from product.serializers import ProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'
        extra_kwargs = {
            'owner': {'required': False},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        validated_data['name'] = self.context['request'].data['name']
        wishlist = Wishlist.objects.create(**validated_data)
        return wishlist


class AddOrDeleteToWishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ['id', 'name', 'product']
        extra_kwargs = {'name': {'required': False}}
