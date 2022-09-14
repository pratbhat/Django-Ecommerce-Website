from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm
import json
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customers = Customer.objects.get_or_create(user=request.user, name=request.user.username, email=request.user.email)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {"total_order_value": 0,
                 "total_quantity": 0}
    return render(request, 'store/products.html', {'products': products,
                                                   'orders': order})


def offered_products(request):
    return HttpResponse('Offer on Products')


def cart(request):
    if request.user.is_authenticated:
        customers = Customer.objects.get_or_create(user=request.user, name=request.user.username,
                                                   email=request.user.email)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"total_order_value": 0,
                 "total_quantity": 0}

    return render(request, 'store/cart.html', {'items': items,
                                               'orders': order})


def checkout(request):
    if request.user.is_authenticated:
        customers = Customer.objects.get_or_create(user=request.user, name=request.user.username,
                                                   email=request.user.email)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"total_order_value": 0,
                 "total_quantity": 0}
    return render(request, 'store/checkout.html', {'items': items,
                                                   'orders': order})


def update_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customers = Customer.objects.get_or_create(user=request.user, name=request.user.username, email=request.user.email)
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, create = Order.objects.get_or_create(customer=customer, complete=False)
    item, create = order.orderitem_set.get_or_create(order=order, product=product)

    if action == "add":
        item.quantity += 1
    elif action == "remove":
        item.quantity -= 1

    item.save()

    if item.quantity <= 0 or action == "delete":
        item.delete()

    return JsonResponse('object updated successfully',safe=False)


def process_data(request):
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customers = Customer.objects.get_or_create(user=request.user, name=request.user.username,
                                                   email=request.user.email)
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
        order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shippinginfo']['address'],
            city=data['shippinginfo']['city'],
            state=data['shippinginfo']['state'],
            zip_code=data['shippinginfo']['zipcode']
        )
    else:
        print('User not logged in.....')

    return JsonResponse('processed data', safe=False)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'store/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('login')

    return render(request, 'store/register.html', {'form': form})


def my_orders(request):
    myorders = {}
    completed_orders = 0
    incomplete_orders = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        myorders = Order.objects.filter(customer=customer, complete=True)
        completed_orders = len(myorders)
        incomplete_orders = len(Order.objects.filter(customer=customer)) - completed_orders
    else:
        order = {"total_order_value": 0,
                 "total_quantity": 0}

    return render(request, 'store/myorders.html', {'myorders': myorders,
                                                   'orders': order,
                                                   'completed_orders': completed_orders,
                                                   'incomplete_orders': incomplete_orders})

