from django.urls import path
from apps.products import views 

urlpatterns = [
    #tela principal
    path('', views.ProductListView.as_view(), name='list'),
    
    #tela de adicionar novo produto
    path('add/', views.ProductCreate.as_view(), name='add'),
    
    #tela de detalhes
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    
    #tela de edição de produto
    path('edit/<int:pk>/', views.ProductUpdate.as_view(), name='edit'),
    
    #tela de deletar produto
    path('delete/<int:pk>/', views.ProductDelete.as_view(), name='delete'),
]
