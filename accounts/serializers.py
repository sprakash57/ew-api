from rest_framework import serializers
from .models import Registration
from django.contrib.auth.hashers import make_password


class RegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ['id', 'email', 'phone', 'password', 'is_admin', 'is_vendor']
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self):
        registration = Registration(
            email=self.validated_data["email"].lower(),
            phone=self.validated_data["phone"],
            password=make_password(self.validated_data["password"]),
            is_admin=self.validated_data["is_admin"],
            is_vendor=self.validated_data["is_vendor"]
        )
        registration.save()
