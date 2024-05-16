from django.contrib import admin

# Register your models here.
from .models import Task, InvoiceHeader, InvoiceItem, InvoiceBillSundry

admin.site.register(Task)
admin.site.register(InvoiceHeader)
admin.site.register(InvoiceItem)
admin.site.register(InvoiceBillSundry)