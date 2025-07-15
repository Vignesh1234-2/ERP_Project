from django.db import models

class Finance(models.Model):
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.transaction_type} - {self.amount}"