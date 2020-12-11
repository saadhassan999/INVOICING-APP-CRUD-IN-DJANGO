from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.invoices_list, name='invoices_list'),
    path('delete/<int:id>', views.deleteInvoice, name='deleteInvoice'),
    path('edit/<int:id>', views.editInvoice, name='editInvoice'),
    path('addInvoices/', views.addInvoices, name='addInvoices'),
]