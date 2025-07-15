from rest_framework import generics
from erp_analytics.models.logistics import Logistics
from erp_analytics.serializers.logistics_serializer import LogisticsSerializer

class LogisticsListCreateView(generics.ListCreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer

class LogisticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer