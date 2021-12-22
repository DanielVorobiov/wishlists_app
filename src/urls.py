
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('api/', include([
        path('user/',include('user.urls')),
        path('product/',include('product.urls')),
        path('wishlist/', include('wishlist.urls'))
    ]))
    
]
