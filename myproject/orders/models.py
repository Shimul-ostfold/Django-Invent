from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254, default='default@example.com')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    style = models.CharField(max_length=255)
    worker_name = models.CharField(max_length=255, blank=True)
    factory_in_date = models.DateField(blank=True, null=True)
    shop_in_date = models.DateField(blank=True, null=True)
    bill_paid_date = models.DateField(blank=True, null=True)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.style

class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment {self.id} - Order {self.order.id}"
