from django.urls import path
from apps.products import views 

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('add/', views.ProductCreate.as_view(), name='add'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.ProductUpdate.as_view(), name='edit'),
    #path('delete/<int:pk>/', AuthorDelete.as_view(), name='delete'),
]
