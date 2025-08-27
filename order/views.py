from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers.order_serializer import OrderSerializer
from drf_yasg.utils import swagger_auto_schema

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by("id")

    @swagger_auto_schema(
        operation_summary="Lista todos os pedidos",
        operation_description="Retorna todos os pedidos com detalhes dos produtos e total",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Cria um novo pedido",
        operation_description="Cria um pedido associando produtos pelo ID e vinculando ao usuário",
        request_body=OrderSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Recupera um pedido",
        operation_description="Retorna os detalhes de um pedido pelo seu ID",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualiza um pedido",
        operation_description="Atualiza os produtos ou usuário de um pedido",
        request_body=OrderSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualização parcial de um pedido",
        operation_description="Permite atualizar apenas alguns campos de um pedido",
        request_body=OrderSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Exclui um pedido",
        operation_description="Remove um pedido pelo seu ID",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
