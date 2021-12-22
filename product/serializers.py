from rest_framework import serializers

from product.models import Product
from wishlist.models import Wishlist


class ProductSerializer(serializers.ModelSerializer):
    nr_of_users_want_it = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_nr_of_users_want_it(self, instance):
        return Wishlist.product.through.objects.filter(product_id=instance.id).values('wishlist__owner').distinct().count()
