from good_deeds.models import GoodDeed
from plans.models import Plan, UrgentMessage
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import (GenericViewSet, ReadOnlyModelViewSet,
                                     ViewSet)
from users.utils import confirm_email, send_confirmation_link_to_email

from .serializers import (GoodDeedSerializer, PlanSerializer,
                          UrgentMessageSerializer, UserSerializer)


class UserViewSet(ViewSet):
    """Класс отображения работы с моделью CustomUser."""

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_link_to_email(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        if request.method == 'PATCH':
            serializer = UserSerializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class EmailConfirmationView(APIView):
    """Класс отображнеия для работы со ссылкой-подтверждением."""

    def get(self, request, uidb64, token):
        try:
            confirm_email(uidb64=uidb64, token=token)
            return Response(
                {'message': 'Адресс почты подтвержден'},
                status=status.HTTP_200_OK
            )
        except (TypeError, ValueError):
            return Response(
                {'message': 'Подтверждающая ссылка недействительна'},
                status=status.HTTP_400_BAD_REQUEST
            )


class PlanViewSet(ReadOnlyModelViewSet):
    """Класс отображения для работы с моделью Plan."""

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class UrgentMessageViewSet(ReadOnlyModelViewSet):
    """Класс отображения для работы с моделью UrgentMessage."""

    queryset = UrgentMessage.objects.all()
    serializer_class = UrgentMessageSerializer


class GoddDeedViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """Класс отображения для работы с моделью GoodDeed."""

    queryset = GoodDeed.objects.all()
    serializer_class = GoodDeedSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
