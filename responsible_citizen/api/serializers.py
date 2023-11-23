from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
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
