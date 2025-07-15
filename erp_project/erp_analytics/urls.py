from django.urls import path

from .views import (
    sales_views,
    inventory_views,
    customer_views,
    forecast_views,
    employee_views,
    finance_views,
    logistics_views,
    supplier_views,
)

urlpatterns = [
    # Sales URLs
    path('sales/', sales_views.SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>/', sales_views.SalesDetailView.as_view(), name='sales-detail'),

    # Inventory URLs
    path('inventory/', inventory_views.InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', inventory_views.InventoryDetailView.as_view(), name='inventory-detail'),

    # Customer URLs
    path('customers/', customer_views.CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', customer_views.CustomerDetailView.as_view(), name='customer-detail'),

    # Forecast URLs
    path('forecasts/', forecast_views.ForecastListCreateView.as_view(), name='forecast-list-create'),
    path('forecasts/<int:pk>/', forecast_views.ForecastDetailView.as_view(), name='forecast-detail'),

    # Employee URLs
    path('employees/', employee_views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', employee_views.EmployeeDetailView.as_view(), name='employee-detail'),

    # Finance URLs
    path('finance/', finance_views.FinanceListCreateView.as_view(), name='finance-list-create'),
    path('finance/<int:pk>/', finance_views.FinanceDetailView.as_view(), name='finance-detail'),

    # Logistics URLs
    path('logistics/', logistics_views.LogisticsListCreateView.as_view(), name='logistics-list-create'),
    path('logistics/<int:pk>/', logistics_views.LogisticsDetailView.as_view(), name='logistics-detail'),

    # Supplier URLs
    path('suppliers/', supplier_views.SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', supplier_views.SupplierDetailView.as_view(), name='supplier-detail'),
]