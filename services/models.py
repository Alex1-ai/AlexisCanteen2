from typing import Iterable
from django.db import models
from django.urls import reverse
import secrets
from .paystack import PayStack
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Services(models.Model):
    serviceName = models.CharField(max_length=70)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True)
    is_active = models.BooleanField(default=False)
    service_image = models.ImageField(
        upload_to='services/images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def get_url(self):
        return reverse('shop_by_services', args=[self.slug])

    def __str__(self):
        return self.serviceName


class Shop(models.Model):
    name = models.CharField(max_length=70)

    price = models.CharField(max_length=70)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to="shops/images", blank=True, null=True)
    services = models.ForeignKey(
        Services, on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('delivery', args=[self.services.serviceName])

    def __str__(self):
        return self.name


class Food(models.Model):

    meal = models.CharField(max_length=255)
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    amount = models.PositiveBigIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return f"Payment: {self.amount} : Verified: {self.verified}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified =  True
            self.save()
        if self.verified:
            return True
        return False


class Order(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    contact = models.CharField(max_length=14)
    package = models.CharField(max_length=277)
    service_shop = models.CharField(max_length=289, default="Testing Service")
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=257)
    num_of_packs = models.CharField(max_length=255)
    contact = models.CharField(max_length=14)
    user_preference = models.TextField(blank=True, null=True)
