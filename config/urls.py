from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from product.views import *

router = SimpleRouter()
router.register('products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/orders/', include('product.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/product/', ProductAPIList.as_view()),
    # path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    # path('api/v1/product-delete/<int:pk>/', ProductAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_name'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
