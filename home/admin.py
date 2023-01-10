"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from . import models

admin.site.site_header = 'ONLINE CANTEEN '
admin.site.index_title = 'Admin'


@admin.register(models.FrequentQuestion)
class FrequentQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'number', ]


@admin.register(models.SupportStaffDetails)
class SupportStaffDetailsAdmin(admin.ModelAdmin):
    list_display = ['location', 'email', 'contact',
                    'open_hours', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link']


@admin.register(models.Testimonies)
class TestimoniesAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'rating',
                    'customer_review', 'is_accepted', 'created_at', 'updated_at']


@admin.register(models.Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['featureName', 'featureIcon']


@admin.register(models.HomePageWords)
class HomePageWordsAdmin(admin.ModelAdmin):
    list_display = ['logo', 'title', 'subtitle']


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
