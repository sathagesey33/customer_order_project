from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets
from .utils import send_sms  


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Save the new order instance
        order = serializer.save()

        # Send an SMS to the customer
        customer_phone = order.customer.phone_number  
        message = f"Thank you for your order, {order.customer.name}. Your order #{order.id} has been received."

        # Call the send_sms function
        response = send_sms(customer_phone, message)

        #  handle the response 
        if response:
            print("SMS sent successfully:", response)
        else:
            print("Failed to send SMS.")
