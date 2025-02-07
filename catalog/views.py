from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, "catalog/product_list.html", context)


def contact(request):
    return render(request, "catalog/contact.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)


