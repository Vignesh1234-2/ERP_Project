from django.db import models

class Logistics(models.Model):
    shipment_id = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    shipped_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.shipment_id