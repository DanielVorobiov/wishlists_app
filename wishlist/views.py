from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer, AddOrDeleteToWishlistSerializer
from wishlist.permissions import IsOwnerOrReadOnly


class WishlistViewset(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    #TODO: Permissions
    @action(detail=True, methods=['POST'], permission_classes=[IsOwnerOrReadOnly])
    def add(self, request, pk):
        wishlist_instance = Wishlist.objects.get(pk=pk)
        serializer = AddOrDeleteToWishlistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product_id = serializer.validated_data['product'][0].id
            if not Wishlist.product.through.objects.filter(product_id=product_id, wishlist_id=pk):
                wishlist_instance.product.add(product_id)
                message = {
                    "message": "Product successfully added to wishlist."}
                return response.Response(message, status=status.HTTP_200_OK)

            message = {"message": "Product already in wishlist."}
            return response.Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(serializer.errors,
                                     status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'], permission_classes=[IsOwnerOrReadOnly])
    def remove(self, request, pk):
        wishlist_instance = Wishlist.objects.get(pk=pk)
        serializer = AddOrDeleteToWishlistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product_id = serializer.validated_data['product'][0].id

            if Wishlist.product.through.objects.filter(product_id=product_id, wishlist_id=pk):
                wishlist_instance.product.remove(product_id)
                message = {
                    "message": "Product successfully removed from wishlist."}
                return response.Response(message, status=status.HTTP_200_OK)

            else:
                message = {"message": "Product is not in wishlist."}
                return response.Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(serializer.errors,
                                     status=status.HTTP_400_BAD_REQUEST)
