from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Invoice)
admin.site.register(InvoiceItem)
