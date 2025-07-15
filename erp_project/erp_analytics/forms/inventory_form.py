from django import forms
from erp_analytics.models.inventory import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'category', 'stock_qty', 'reorder_level']