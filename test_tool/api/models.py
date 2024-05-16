from django.db import models
from django.contrib.auth.models import User
import uuid

class Task(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class InvoiceHeader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    invoice_number = models.IntegerField(null=False,unique=True)
    customer_name = models.CharField(max_length=100)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    gstin = models.CharField(max_length=15 )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class InvoiceBillSundry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bill_sundary_name = models.CharField(max_length=100,)
    amount = models.DecimalField(max_digits=10, decimal_places=2,)
    

