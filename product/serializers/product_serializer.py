from rest_framework import serializers
from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer
from drf_yasg.utils import swagger_serializer_method
from drf_yasg import openapi

class ProductSerializer(serializers.ModelSerializer):
    # Mostra categorias detalhadas (read-only)
    category = CategorySerializer(read_only=True, many=True, help_text="Categorias detalhadas do produto")
    
    # Permite associar categorias pelo ID no create/update
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True,
        help_text="IDs das categorias associadas ao produto"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]
        extra_kwargs = {
            "title": {"help_text": "Nome do produto", "min_length": 1, "max_length": 100},
            "description": {"help_text": "Descrição detalhada do produto", "max_length": 500},
            "price": {"help_text": "Preço em centavos", "min_value": 0},
            "active": {"help_text": "Se o produto está ativo ou não"},
        }

    def create(self, validated_data):
        categories_data = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.category.set(categories_data)
        return product

    def update(self, instance, validated_data):
        # Atualiza categorias se forem passadas
        if "categories_id" in validated_data:
            categories_data = validated_data.pop("categories_id")
            instance.category.set(categories_data)
        return super().update(instance, validated_data)

