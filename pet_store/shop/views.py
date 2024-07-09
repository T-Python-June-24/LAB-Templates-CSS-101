from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'shop/base.html')

def contact(request):
    return render(request, 'shop/contact.html')

def get_cat_products():
    products = [
        {
            'id': 1,
            'name': 'Cat Food',
            'description': 'Cat Dry Food "Chicken"',
            'image': 'images/cf1.jpg',
            'price': '80.00'
        },
        {
            'id': 2,
            'name': 'Cat Food 2',
            'description': 'Cat Dry Food "Fillet O Flakes"',
            'image': 'images/cf2.jpg',
            'price': '85.00'
        },
        {
            'id': 3,
            'name': 'Cat Food 3',
            'description': 'Cat Dry Food "For Kitten & Pregnant Cat"',
            'image': 'images/cf3.jpg',
            'price': '80.00'
        },
        {
            'id': 4,
            'name': 'Cat Food 4',
            'description': 'Cat Dry Food "Classic"',
            'image': 'images/cf4.jpg',
            'price': '85.00'
        },{
            'id': 5,
            'name': 'Cat Toy 1',
            'description': 'Cat Toy',
            'image': 'images/ct1.jpg',
            'price': '30.00'
        },
        {
            'id': 6,
            'name': 'Cat Toy 2',
            'description': 'Cat Toy 2',
            'image': 'images/ct2.jpg',
            'price': '35.00'
        },{
            'id': 7,
            'name': 'Cat Toy 3',
            'description': 'Cat Toy 3',
            'image': 'images/ct3.jpg',
            'price': '40.00'
        },
        {
            'id': 8,
            'name': 'Cat Toy 4',
            'description': 'Cat Toy 4',
            'image': 'images/ct4.jpg',
            'price': '45.00'
        },
    ]
    return products

def get_dog_products():
    products= [
        {
            'id': 9,
            'name': 'Dog Food 1',
            'description': 'Dog Dry Food "Master Mix"',
            'image': 'images/df1.jpg',
            'price': '80.00'
        },
        {
            'id': 10,
            'name': 'Dog Food 2',
            'description': 'Dog Dry Food "Junior"',
            'image': 'images/df2.jpg',
            'price': '85.00'
        },
        {
            'id': 11,
            'name': 'Dog Food 3',
            'description': 'Dog Dry Food "Alpha Adult"',
            'image': 'images/df3.jpg',
            'price': '90.00'
        },
        {
            'id': 12,
            'name': 'Dog Food 4',
            'description': 'Dog Dry Food "Classic"',
            'image': 'images/df4.jpg',
            'price': '95.00'
        },{
            'id': 13,
            'name': 'Dog Toy 1',
            'description': 'Dog Toy',
            'image': 'images/dt1.jpg',
            'price': '30.00'
        },
        {
            'id': 14,
            'name': 'Dog Toy 2',
            'description': 'Dog Toy 2',
            'image': 'images/dt2.jpg',
            'price': '35.00'
        },{
            'id': 15,
            'name': 'Dog Toy 3',
            'description': 'Dog Toy 3',
            'image': 'images/dt3.jpg',
            'price': '40.00'
        },
        {
            'id': 16,
            'name': 'Dog Toy 4',
            'description': 'Dog Toy 4',
            'image': 'images/dt4.jpg',
            'price': '45.00'
        },
    ]
    return products

def cat_page(request):
    cat_products = get_cat_products()
    context = {'products': cat_products}
    return render(request, 'shop/cat_page.html', context)

def dog_page(request):
    dog_products = get_dog_products()
    context = {'products': dog_products}
    return render(request, 'shop/dog_page.html', context)

def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        product = next((p for p in get_cat_products() + get_dog_products() if p['id'] == product_id), None)
        if product:
            cart = request.session.get('cart', [])
            cart.append({'product': product, 'quantity': quantity})
            request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    order_number = request.session.get('order_number', 1)
    context = {'cart': cart, 'order_number': order_number}
    return render(request, 'shop/view_cart.html', context)

from django.shortcuts import render, redirect

def view_cart(request):
    cart = request.session.get('cart', [])
    total = 0
    for item in cart:
        quantity = int(item['quantity'])  
        price = float(item['product']['price'])  
        item_total = quantity * price
        total += item_total
    return render(request, 'shop/view_cart.html', {'cart': cart, 'total': total})


def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        if 'update' in request.POST:
            product_id = int(request.POST['update'])
            new_quantity = int(request.POST.get('quantities', 1))
            for item in cart:
                if item['product']['id'] == product_id:
                    item['quantity'] = new_quantity
                    break
        elif 'remove' in request.POST:
            product_id = int(request.POST['remove'])
            cart = [item for item in cart if item['product']['id'] != product_id]

        request.session['cart'] = cart
        return redirect('view_cart')

