from rest_framework import serializers
from .models import Task, InvoiceHeader, InvoiceItem, InvoiceBillSundry
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class InvoiceHeaderListCreateSerializer(serializers.ModelSerializer):

    # def get(self, request):
    #     invoice = InvoiceHeader.objects.all()
    #     serializer = InvoiceHeaderSerializer(invoice, many=True)
    #     if serializer_is_valid():
    #         # TotalAmount = Sum(InvoiceItems’s Amount) + Sum(InvoiceBillSundry’s Amount)
    #         serializer.save()
    #     return Response(serializer.data)
    # def validate(self, data):
    #     # TotalAmount = Sum(InvoiceItems’s Amount) + Sum(InvoiceBillSundry’s Amount)
    #     sum_of_total_amount = data.invoiceitem_set.all().aggregate(Sum('amount')) + data.invoicebillsundry_set.all().aggregate(Sum('amount'))
    #     if data.total_amount == sum_of_total_amount:
            
    #         return data
    
    class Meta:
        model = InvoiceHeader
        fields = '__all__'

class InvoiceHeaderRetrieveUpdateDestroySerializer(serializers.ModelSerializer):


    class Meta:
        model = InvoiceHeader
        fields = '__all__'


class InvoiceItemListCreateSerializer(ListCreateAPIView):

    class Meta:
        model = InvoiceItem
        fields = '__all__'



class InvoiceItemRetrieveUpdateDestroySerializer(RetrieveUpdateDestroyAPIView):
    class Meta:
        model = InvoiceItem
        fields = '__all__'


class InvoiceBillSundryListCreateSerializer(ListCreateAPIView):
    
        class Meta:
            model = InvoiceBillSundry
            fields = '__all__'

class InvoiceBillSundryRetrieveUpdateDestroySerializer(RetrieveUpdateDestroyAPIView):

    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'