from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EmployeeDb
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class EmployeeSerilier(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDb
        fields = "__all__"
        