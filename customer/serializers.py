from .models import Details
from rest_framework import serializers

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['name', 'email', 'password']