from rest_framework import generics, permissions
from .models import Task, InvoiceHeader, InvoiceItem, InvoiceBillSundry
from .serializers import TaskSerializer, InvoiceHeaderListCreateSerializer, InvoiceHeaderRetrieveUpdateDestroySerializer, InvoiceItemListCreateSerializer, InvoiceItemRetrieveUpdateDestroySerializer, InvoiceBillSundryListCreateSerializer, InvoiceBillSundryRetrieveUpdateDestroySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]



class InvoiceHeaderListCreate(generics.ListCreateAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderListCreateSerializer


class InvoiceHeaderRetrieveUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderRetrieveUpdateDestroySerializer


