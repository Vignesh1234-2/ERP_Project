from rest_framework import generics
from erp_analytics.models.finance import Finance
from erp_analytics.serializers.finance_serializer import FinanceSerializer

class FinanceListCreateView(generics.ListCreateAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

class FinanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer