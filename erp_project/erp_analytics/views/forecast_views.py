from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..ml_utils import run_forecast

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def run_revenue_forecast(request):
    prediction = run_forecast()
    return Response({"predicted_revenue": prediction})
