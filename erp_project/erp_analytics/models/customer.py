from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    segment = models.CharField(max_length=50)
    last_purchase = models.DateField()

    def _str_(self):
        return self.name