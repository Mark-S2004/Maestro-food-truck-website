from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def menu(request):
    return render(request, 'order/menu.html')

def cart(request):
    return render(request, 'order/cart.html')

def checkout(request):
    return render(request, 'order/checkout.html')

def addToCart(request):
    if request.method == 'POST':
        menu_item = request.POST["menu-item"]
        count = getattr(request.user, menu_item)
        setattr(request.user, menu_item, count+1)
        request.user.save()
        return HttpResponseRedirect(reverse("menu"))