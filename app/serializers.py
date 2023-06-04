from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['device_type', 'description', 'device_id', 'company', 'user', 'checked_out_at', 'returned_at', 'status', 'checkedOutCondition', 'returnCondition']

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'company']