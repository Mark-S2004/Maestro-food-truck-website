from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu, name="menu"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('add-to-cart', views.addToCart, name="add-to-cart"),
    path('set-cart-item', views.setCart, name='set-cart')
]