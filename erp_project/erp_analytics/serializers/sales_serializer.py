from rest_framework import viewsets
from erp_analytics.models.sales import Sales
from erp_analytics.serializers.sales_serializer import SalesSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer