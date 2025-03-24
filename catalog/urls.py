from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("contacts/", ContactListView.as_view(), name="contact_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
