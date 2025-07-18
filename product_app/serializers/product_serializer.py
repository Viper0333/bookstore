from rest_framework import serializers
from product_app.models.product import Product
from product_app.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)


    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category',
        ]
