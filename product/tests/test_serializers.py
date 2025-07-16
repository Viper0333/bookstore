from django.test import TestCase
from product.models.category import Category
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class ProductSerializerTest(TestCase):
    def test_valid_data(self):
        category = Category.objects.create(title="Tech", slug="tech", description="Tech stuff", active=True)
        product = Product.objects.create(title="Mouse", description="Wireless", price=120, active=True)
        product.category.add(category)

        serializer = ProductSerializer(instance=product)
        data = serializer.data

        self.assertEqual(data['title'], "Mouse")
        self.assertEqual(data['description'], "Wireless")
        self.assertEqual(data['price'], 120)
