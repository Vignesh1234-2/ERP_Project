from django.db import models

class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    reorder_level = models.IntegerField()

    def _str_(self):
        return self.product_name