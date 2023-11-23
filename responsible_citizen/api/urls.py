from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView)

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/login/', TokenObtainPairView.as_view(), name='token_login'),
    path(
        'v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh,'
    ),
    path(
        'v1/token/logout/', TokenBlacklistView.as_view(), name='token_logout'
    ),
]
