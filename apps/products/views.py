# Create your views here.
from django.views.generic import ListView
from apps.products.models import Product


class ProductListView(ListView):
    model = Product
    
