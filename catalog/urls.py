from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="product_list"),
    path("contacts/", contact, name="contacts"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]
