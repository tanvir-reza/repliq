from django.contrib import admin

# Register your models here.
from .models import Asset, Company, User


class AssetAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'description', 'company', 'user', 'checked_out_at', 'returned_at', 'status')
    list_filter = ('company', 'user', 'status')

admin.site.register(Asset, AssetAdmin)
admin.site.register(Company)
admin.site.register(User)
