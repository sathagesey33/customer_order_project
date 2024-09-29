from django.urls import path
from .views import CustomerCreateView, OrderCreateView

urlpatterns = [
    path('customers/', CustomerCreateView.as_view(), name='create-customer'),
    path('orders/', OrderCreateView.as_view(), name='create-order'),
]
