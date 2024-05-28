from rest_framework import serializers

from .models import *

# Serializers define the API representation.
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'