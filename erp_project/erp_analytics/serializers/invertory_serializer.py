from rest_framework import viewsets
from erp_analytics.models.inventory import Inventory
from erp_analytics.serializers.inventory_serializer import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer