"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    name = factory.Faker("name")
    description = factory.Faker("text")
    price = FuzzyDecimal(100, 1000)
    category = factory.SubFactory(CategoryFactory)

    def create(self):
        """Creates a fake product and returns it"""

        product = Product(
            name=self.name,
            description=self.description,
            price=self.price,
            category=self.category,
        )
        product.save()
        return product


class CategoryFactory(factory.Factory):
    """Creates fake categories for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Category

    name = factory.Faker("name")

    def create(self):
        """Creates a fake category and returns it"""

        category = Category(name=self.name)
        category.save()
        return category
