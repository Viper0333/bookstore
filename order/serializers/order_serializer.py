from rest_framework import serializers
from product.models import Product
from product.serializers.product_serializer import ProductSerializer
from order.models import Order  # Importa o modelo correto

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        return sum([product.price for product in instance.product.all()])

    class Meta:
        model = Order 
        fields = ['user', 'product', 'total']
        # fields = ['product', 'total']
