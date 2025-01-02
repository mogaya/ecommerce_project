from rest_framework import serializers
from .models import Product, Order, OrderItem, Category

# Start Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only= True)

    class Meta:
        model = Product
        fields = ['name','description','price','stock_quantity','category_name','image_url','created_date']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value
    
    def validate_stock_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Stock Quantity must be greater than zero")
        return value
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        
        if len(value) < 3:
            raise serializers.ValidationError("Name must be atleast 3 characters long")
        
        if len(value) > 30:
            raise serializers.ValidationError("Name cannot exceed 30 characters")
        
        return value 

# Start OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'quantity', 'subtotal']
        read_only_fields = ['subtotal'] 

# Start Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only= True)
    total_price = serializers.IntegerField(read_only= True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'status', 'created_date']
        read_only_fields = ['user', 'total_price', 'status', 'created_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = validated_data['user']

        # create order
        order = Order.objects.create(user=user)

        total_price = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            if quantity > product.stock_quantity:
                raise serializers.ValidationError(f"Insufficient stock for product: {product.name}")
            
            subtotal = product.price * quantity
            total_price += subtotal

            # Stock Quantity is automatically reduced when an order is placed
            product.stock_quantity -= quantity
            product.save()

            # Create OrderItem
            OrderItem.objects.create(order=order, product=product, quantity=quantity, subtotal=subtotal )

        order.total_price = total_price
        order.save()

        return order

# Start Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
