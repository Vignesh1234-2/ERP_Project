from django import forms
from erp_analytics.models.forecast import Forecast

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = ['month', 'predicted_revenue', 'actual_revenue']