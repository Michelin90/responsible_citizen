from plans.models import Plan, UrgentMessage
from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class UserSerializer(ModelSerializer):
    """Сериализатор модели CustomUser."""

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'phone_number'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PlanSerializer(ModelSerializer):
    """Сериализатор модели Plans."""

    class Meta:
        model = Plan
        fields = [
            'id',
            'description',
            'image',
            'stage',
            'pdf_file',
            'created_at'
        ]


class UrgentMessageSerializer(ModelSerializer):
    """Сериализатор модели UrgentMessage."""

    class Meta:
        model = UrgentMessage
        fields = [
            'id',
            'description',
            'image',
            'created_at'
        ]
