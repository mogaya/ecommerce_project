from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, OrderItem, Category
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# Start Category ViewSet
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Start Product ViewSet
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# Start OrderItem ViewSet
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

# Start Order ViewSet
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # users see only their own orders
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # set user for the order automatically
        serializer.save(user=self.request.user)
    