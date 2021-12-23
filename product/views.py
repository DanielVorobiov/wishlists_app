from rest_framework import viewsets

from product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
