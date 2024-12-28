from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

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