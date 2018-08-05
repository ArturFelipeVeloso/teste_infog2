# Create your views here.
from django.views.generic import ListView
from apps.products.models import Product
from apps.products.forms import ProductForm

from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/add.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/edit.html"

class ProductDelete(DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = '/'
