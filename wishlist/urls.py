from wishlist.views import WishlistViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', WishlistViewset, basename='wishlist')
urlpatterns = router.urls