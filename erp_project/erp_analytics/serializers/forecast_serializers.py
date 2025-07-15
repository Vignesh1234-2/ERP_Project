from rest_framework.views import APIView
from rest_framework.response import Response
from erp_analytics.models.forecast import Forecast
from erp_analytics.serializers.forecast_serializer import ForecastSerializer

class ForecastRunView(APIView):
    def post(self, request):
        # Dummy ML prediction logic
        forecast = Forecast.objects.create(
            month="August 2025",
            predicted_revenue=123456.78
        )
        serializer = ForecastSerializer(forecast)
        return Response(serializer.data)