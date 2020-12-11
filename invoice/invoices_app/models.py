from django.db import models

# Create your models here.
class Invoice(models.Model):
    item = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.item