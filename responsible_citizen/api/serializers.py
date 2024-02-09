from rest_framework.serializers import ModelSerializer
from users.models import CustomUser
from plans.models import Plan


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
            'description',
            'image',
            'stage',
            'pdf_file'
        ]
