from django import forms
from erp_analytics.models.employee import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'attendance_status', 'date']
        
        