from rest_framework import serializers
from .models import Member
from django.contrib.auth import get_user_model

User = get_user_model()


class MemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Member
        fields = ["id", "username", "email", "role", "manager", "user"]


class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["user", "role", "manager"]
