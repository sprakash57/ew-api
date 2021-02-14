from rest_framework import serializers
from .models import Registration


class RegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ['email', 'phone', 'password', 'role']
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self):
        registration = Registration(
            email=self.validated_data["email"].lower(),
            phone=self.validated_data["phone"],
            role=self.validated_data["role"],
            password=self.validated_data["password"]
        )
        registration.save()
