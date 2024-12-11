from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    return render(request, 'inventory/product_list.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

def cart_view(request):
    cart = request.session.get('cart', [])
    total = sum(item['quantity'] * item['product'].price for item in cart)
    return render(request, 'inventory/cart.html', {'cart': cart, 'total': total})

def checkout(request):
    total = request.session.get('total', 0)
    return render(request, 'inventory/checkout.html', {'total': total})

def home(request):
    return render(request, 'inventory/home.html')  # Ensure 'home.html' exists