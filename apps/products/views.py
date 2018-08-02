# Create your views here.
from django.views.generic import ListView
from apps.products.models import Product
from apps.products.forms import ProductForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.generic import DetailView


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
