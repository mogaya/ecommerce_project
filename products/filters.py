from django_filters import rest_framework as filters
from .models import Product

# Product Filter Class
class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    in_stock = filters.BooleanFilter(method='filter_in_stock')
    category = filters.CharFilter(field_name="category__name", lookup_expr='icontains')
    

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
    # Filters products based on stock availability. `True` means products with stock > 0. `False` means products with stock == 0.
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset.filter(stock_quantity__lte=0)