from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product', help_text='Product')
    description = models.TextField(verbose_name='description', help_text='Product description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price', help_text='price')
    image = models.ImageField(upload_to="products/images", blank=True, null=True, verbose_name='image', help_text='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "products"
        verbose_name = "products"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField

    class Meta:
        verbose_name_plural = "categories"
        verbose_name = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
