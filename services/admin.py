from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "package", "location", "address",
                    "num_of_packs", "contact", "email", "user_preference"]

    list_display_links = ["name", "package", "location", "address",
                          "num_of_packs", "contact", "email", "user_preference"]


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    prepopulated_fiels = {'slug': ('name',)}
    list_display = ['name', 'price', 'image', 'slug',
                    'services',  'is_active',  'created_at', 'updated_at']
    list_display_links = [
        'name', 'slug', 'services', 'price', 'created_at', 'is_active'
    ]


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['meal', 'shop', 'created_at', 'updated_at']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject',
                    'message', 'created_at', 'updated_at']

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount', 'email', 'ref',
                    'date_created', 'verified']


@admin.register(models.Services)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_field = {'slug': ('serviceName',)}
    list_display = ['serviceName', 'title',
                    'service_image', 'created_at', 'slug', 'is_active']

    list_display_links = ['slug', 'serviceName']
