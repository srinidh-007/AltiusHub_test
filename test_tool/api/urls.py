from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, InvoiceHeaderListCreate, InvoiceHeaderRetrieveUpdateDestroy

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('invoiceheader/', InvoiceHeaderListCreate.as_view(), name='invoiceheader-list'),
    path('invoiceheader/<uuid:pk>/', InvoiceHeaderRetrieveUpdateDestroy.as_view(), name='invoiceheader-detail'),
    # path('invoiceitem/', InvoiceItemListCreate.as_view(), name='invoiceitem-list'),
    # path('invoiceitem/<uuid:pk>/', InvoiceItemRetrieveUpdateDestroy.as_view(), name='invoiceitem-detail'),
    # path('invoicebillsundry/', InvoiceBillSundryListCreate.as_view(), name='invoicebillsundry-list'),
    # path('invoicebillsundry/<uuid:pk>/', InvoiceBillSundryRetrieveUpdateDestroy.as_view(), name='invoicebillsundry-detail'),
]
 