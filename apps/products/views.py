# Create your views here.
from django.views.generic import ListView
from apps.products.models import Product
from apps.products.forms import ProductForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class ProductListView(ListView):
    model = Product
    

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
