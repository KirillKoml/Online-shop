from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    last_display = ('id', 'name', 'price', 'category')
    last_filter = ('product',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    last_display = ('id', 'name')
