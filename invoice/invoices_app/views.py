from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from .forms import AddInvoice

# Create your views here.
def invoices_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices_app/invoices_list.html', {'invoices' : invoices})

def addInvoices(request):
    if request.method == 'POST':
        form = AddInvoice(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices_app:invoices_list')
    else:
        form = AddInvoice
    return render(request, 'invoices_app/add_invoices.html', {'form' : form})

def deleteInvoice(request, id):
    invo = Invoice.objects.get(id=id)
    invo.delete()
    return redirect('invoices_app:invoices_list')

def editInvoice(request, id):
    if request.method == "POST":
        invo_form = Invoice.objects.get(id=id)
        frm = AddInvoice(request.POST, instance=invo_form)
        if frm.is_valid():
            frm.save()
            return redirect('invoices_app:invoices_list')
    else:
        invo_form = Invoice.objects.get(id=id)
        frm = AddInvoice(instance=invo_form)
    return render(request, 'invoices_app/edit_invoices.html', {'form' : frm})