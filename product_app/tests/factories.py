import factory

from product_app.models import Product
from product_app.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
    
    class Meta:
        model = Product
