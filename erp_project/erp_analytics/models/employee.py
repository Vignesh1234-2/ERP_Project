from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    attendance_status = models.CharField(max_length=20)
    date = models.DateField()

    def _str_(self):
        return self.name