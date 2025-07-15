from django import forms
from erp_analytics.models.sales import Sales

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product_id', 'region', 'quantity', 'price', 'date']