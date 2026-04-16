from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    products = Product.objects.filter(user=request.user)
    total = products.count()
    low_stock = products.filter(quantity__lt=5).count()

    return render(request, 'dashboard/dashboard.html', {
        'products': products,
        'total': total,
        'low_stock': low_stock
    })

@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']

        Product.objects.create(
            user=request.user,
            name=name,
            quantity=quantity,
            price=price
        )
        return redirect('dashboard')

    return render(request, 'dashboard/add_product.html')