

# Create your models here.
# models.py
from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    # Add other fields as needed

class InvoiceItem(models.Model):
    invoice_number = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed
