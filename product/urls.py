from product.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet, basename='product')
urlpatterns = router.urls
