from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from .models import Asset, User
from .serializers import AssetSerializer, UserSerializer

# Create and List Asset
class AssetListCreate(ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

#View Single Asset
class AssetView(ListAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_field = "device_id"
    def filter_queryset(self, queryset):
        return queryset.filter(device_id=self.kwargs.get("device_id"))

# Create and List User
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve, Update and Destroy Asset by device_id
class AssetRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_field = "device_id"
    def filter_queryset(self, queryset):
        return queryset.filter(device_id=self.kwargs.get("device_id"))

    