# views.py
from django.shortcuts import render, redirect
from app.models import *
from app.forms import *

def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        item_formset = InvoiceItemFormSet(request.POST, prefix='items')

        if invoice_form.is_valid() and item_formset.is_valid():
            invoice = invoice_form.save()
            items = item_formset.save(commit=False)
            for item in items:
                item.invoice = invoice
                item.save()
            return redirect('invoice_detail', invoice_id=invoice.id)
    else:
        invoice_form = InvoiceForm()
        item_formset = InvoiceItemFormSet(prefix='items')

    return render(request, 'create_invoice.html', {'invoice_form': invoice_form, 'item_formset': item_formset})

def view_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    return render(request, 'invoice_detail.html', {'invoice': invoice})
