from django.urls import path
from apps.api import views

app_name = 'api'

urlpatterns = [
    path(
        'products/',
        views.ProductList.as_view(),
        name='product-list'),
    path(
        'products/<int:pk>/',
        views.ProductDetail.as_view(),
        name='product-detail'),
]
