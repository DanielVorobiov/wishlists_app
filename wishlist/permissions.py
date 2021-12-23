from rest_framework import permissions

from wishlist.models import Wishlist


class WishlistPermissions(permissions.BasePermission):
    message = "Must be wishlist owner."

    def has_permission(self, request, view):
        return Wishlist.objects.get(id=view.kwargs['pk']).owner == request.user
