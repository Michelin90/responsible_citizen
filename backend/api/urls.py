from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView)

from .views import (EmailConfirmationView, GoddDeedViewSet, PlanViewSet,
                    UrgentMessageViewSet, UserViewSet)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('plans', PlanViewSet, basename='plans')
router.register(
    'urgent_messages', UrgentMessageViewSet, basename='urgent_messages'
)
router.register('good_deeds', GoddDeedViewSet, basename='good_deeds')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/login/', TokenObtainPairView.as_view(), name='token_login'),
    path(
        'v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh,'
    ),
    path(
        'v1/token/logout/', TokenBlacklistView.as_view(), name='token_logout'
    ),
    path(
        'v1/confirm/<str:uidb64>/<str:token>/',
        EmailConfirmationView.as_view(),
        name='email_confirmation'
    ),
]
