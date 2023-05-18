from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'order/menu.html')

def cart(request):
    return render(request, 'order/cart.html')

def checkout(request):
    return render(request, 'order/checkout.html')