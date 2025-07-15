from rest_framework import generics
from erp_analytics.models.employee import Employee
from erp_analytics.serializers.employee_serializer import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer