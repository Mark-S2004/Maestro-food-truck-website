from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from order.models import MenuItems

# Create your views here.
def menu(request):
    return render(request, 'order/menu.html')

def cart(request):
    menu_items = [('OriginalB', 0, 0), ('ViolaB', 0, 0), ('ChiliB', 0, 0), ('MaestroB', 0, 0), ('HardRockB', 0, 0), ('BeethovenB', 0, 0), ('OriginalC', 0, 0), ('RanchC', 0, 0), ('SticksC', 0, 0), ('StripsC', 0, 0)]
    items_count = list(map(lambda item: (item[0], getattr(MenuItems.objects.get(name=item[0]), 'price'), getattr(request.user, item[0])), menu_items))
    return render(request, 'order/cart.html', context={
        "menu_items": items_count
    })

def checkout(request):
    return render(request, 'order/checkout.html')

def addToCart(request):
    if request.method == 'POST':
        menu_item = request.POST["menu-item"]
        count = getattr(request.user, menu_item)
        setattr(request.user, menu_item, count+1)
        request.user.save()
        return HttpResponseRedirect(reverse("menu"))
    
def setCart(request):
    if request.method == 'POST':
        menu_item = request.POST["menu-item"]
        count = request.POST["count"]
        setattr(request.user, menu_item, count)
        request.user.save()
        return HttpResponseRedirect(reverse("cart"))