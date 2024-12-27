from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# Product ViewSet
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    