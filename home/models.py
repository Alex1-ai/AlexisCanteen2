from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# Create your models here.
"""Declare models for YOUR_APP app."""


class FrequentQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()


class SupportStaffDetails(models.Model):
    location = models.CharField(max_length=288)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    open_hours = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=500, null=True, blank=True)
    facebook_link = models.CharField(max_length=500, null=True, blank=True)
    instagram_link = models.CharField(max_length=500, null=True, blank=True)
    linkedin_link = models.CharField(max_length=500, null=True, blank=True)


class Testimonies(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254, )
    job_title = models.CharField(max_length=80)
    rating = models.IntegerField()
    customer_review = models.TextField()
    is_accepted = models.BooleanField(default=False,)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now_add=True)


class HomePageWords(models.Model):
    logo = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254)


class Features(models.Model):
    # LOCATION_CHOICES = (
    #     ('icon', 'icon'),
    #     ('bi bi-easel', 'bi bi-easel'),
    #     ('bi bi-gem', 'bi bi-gem'),
    #     ('bi bi-geo-alt', 'bi bi-geo-alt'),
    #     ('AshantiRegion', 'AshantiRegion'),

    # )
    featureName = models.CharField(max_length=254)
    featureIcon = models.CharField(max_length=254)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
