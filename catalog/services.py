from django.core.cache import cache

from catalog.models import Product
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