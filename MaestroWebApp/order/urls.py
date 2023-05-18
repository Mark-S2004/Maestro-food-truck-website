from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu, name="menu"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout")
]