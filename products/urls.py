from django.urls import path
from .views import list_products, add_product

urlpatterns = [
    path('list/', list_products, name='list_products'),
    path('add/', add_product, name='add_product'),
]
