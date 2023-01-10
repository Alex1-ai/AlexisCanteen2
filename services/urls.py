from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.store, name="store"),
    path('<slug:services_slug>', views.store, name="shop_by_services"),
    path('delivery/<str:service>/<str:shop_name>/',
         views.delivery, name="delivery"),
    path('contact/', views.contact, name='contact'),
    path('delivery_form/', views.deliveryForm, name='delivery_form'),
    # path('')
    # path('reviewForm/', views.reviewForm, name='reviewForm'),
    # path("review/", views.review, name="review")
]
