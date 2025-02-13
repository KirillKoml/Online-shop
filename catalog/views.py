from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "category", "description", "price", "image", "data_bd")
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "image", "data_bd")
    success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_detail')


class ContactListView(ListView):
    model = Contact
