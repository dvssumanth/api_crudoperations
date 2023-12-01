# forms.py
from django import forms
from app.models import Invoice, InvoiceItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'due_date','due_date']  # Add other fields as needed

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['invoice_number','product_name', 'quantity', 'unit_price']  # Add other fields as needed
