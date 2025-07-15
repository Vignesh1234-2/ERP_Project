from django.db import models

class Sales(models.Model):
    product_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def str(self):
        return f"{self.product_id} - {self.region}"