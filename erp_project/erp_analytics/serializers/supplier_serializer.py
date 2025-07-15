from rest_framework import generics
from erp_analytics.models.supplier import Supplier
from erp_analytics.serializers.supplier_serializer import SupplierSerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer