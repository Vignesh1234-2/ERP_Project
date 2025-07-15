from rest_framework import viewsets
from erp_analytics.models.customer import Customer
from erp_analytics.serializers.customer_serializer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer