
from django.contrib import admin
from django.urls import path
from app.views import AssetListCreate, AssetRetrieveUpdateDestroy, UserListCreate, AssetView

urlpatterns = [
    path('admin/', admin.site.urls),
    #Define the URLS for the API 
    path('api/assets/', AssetListCreate.as_view()),
    # Define the URLS for the API
    path('api/asset/<str:device_id>/', AssetRetrieveUpdateDestroy.as_view()),
    # Define the URLS for the API
    path('api/user', UserListCreate.as_view()),

]
