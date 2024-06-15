from django.shortcuts import render, get_object_or_404
from .models import Customer, Order, OrderItem, Payment

def index(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})
