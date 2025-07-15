from django import forms
from erp_analytics.models.finance import Finance

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['transaction_type', 'amount', 'date', 'description']