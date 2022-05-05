from rest_framework import serializers
from user.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id", "name", "lastName", "cpf", "phone", "birthDay")