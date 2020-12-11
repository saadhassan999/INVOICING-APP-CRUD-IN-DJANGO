from django import forms
from .models import Invoice

class AddInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['item', 'description', 'unit_cost']