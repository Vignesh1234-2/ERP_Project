from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.inventory import Inventory
from ..serializers import InventorySerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_inventory(request):
    inventory = Inventory.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_inventory(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Inventory item added"})
    return Response(serializer.errors)
