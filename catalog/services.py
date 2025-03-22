from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED

def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product


def get_category_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category"
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category