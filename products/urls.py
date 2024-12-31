from .views import ProductViewSet, OrderViewSet, OrderItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('orderItems', OrderItemViewSet, basename='orderItems')

urlpatterns = [
    
]+router.urls
