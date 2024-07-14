from model_bakery import baker
from catalog.models import Category, Product


def sample_category(**kwargs):
    return baker.make(Category, **kwargs)


def sample_product(**kwargs):
    return baker.make(Product, **kwargs)
