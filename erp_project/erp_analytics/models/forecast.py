from django.db import models

class Forecast(models.Model):
    month = models.CharField(max_length=20)
    predicted_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    actual_revenue = models.DecimalField(max_digits=15, decimal_places=2)

    def _str_(self):
        return self.month