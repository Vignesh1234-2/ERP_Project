from django import forms
from erp_analytics.models.customer import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'segment', 'last_purchase']