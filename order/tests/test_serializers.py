from django.test import TestCase
from django.contrib.auth.models import User
from order.models import Order
from product_app.models.product import Product
from order.serializers.order_serializer import OrderSerializer

class OrderSerializerTest(TestCase):
    def test_order_serializer(self):
        user = User.objects.create(username="alex", email="alex@example.com")
        product = Product.objects.create(title="Mouse", description="Wireless", price=120, active=True)
        order = Order.objects.create(user=user)
        order.product.add(product)

        serializer = OrderSerializer(instance=order)
        data = serializer.data

        self.assertEqual(data['user'], user.id)
        self.assertEqual(len(data['product']), 1)
