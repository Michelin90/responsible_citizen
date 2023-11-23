from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdminUser]

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        if request.method == 'PATCH':
            serializer = self.serializer_class(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
