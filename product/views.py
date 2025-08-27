from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer
from product.serializers.category_serializer import CategorySerializer
from drf_yasg.utils import swagger_auto_schema

# ViewSet para produtos
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")

    @swagger_auto_schema(
        operation_summary="Lista todos os produtos",
        operation_description="Retorna todos os produtos cadastrados, incluindo suas categorias detalhadas",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Cria um novo produto",
        operation_description="Cria um produto e associa às categorias pelo ID",
        request_body=ProductSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Recupera um produto",
        operation_description="Retorna os detalhes de um produto pelo seu ID",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualiza um produto",
        operation_description="Atualiza os dados de um produto pelo seu ID. É possível atualizar categorias também",
        request_body=ProductSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualização parcial de um produto",
        operation_description="Permite atualizar apenas alguns campos de um produto",
        request_body=ProductSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Exclui um produto",
        operation_description="Remove um produto pelo seu ID",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# ViewSet para categorias
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")

