from rest_framework import serializers
from .models import LicenseVerification

class LicenseVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseVerification
        fields = '__all__'
