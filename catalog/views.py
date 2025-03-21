from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Contact
from catalog.services import get_product_from_cache


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    login_url = "/user/login/"
    redirect_field_name = '/'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.author = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ("name", "description", "price", "image", "data_bd")
    success_url = reverse_lazy('catalog:product_list')

    login_url = "/user/login/"
    redirect_field_name = '/'

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


    def get_form_class(self):

        # ������� ������ � ������������
        user = self.request.user

        # ���� ������������ ��������, �� �� ����� ������������� ���� ������� � ������������ ������
        if user == self.object.author:
            return ProductForm

        # ���� ������������ ���������, �� �� ����� ������������� ������� � ������������ �� ������ ������������
        if user.has_perm('catalog.may_cancel_publication_product') and user.has_perm(
                'catalog.can_change_description_product') and user.has_perm('catalog.can_change_category_product'):
            return ProductModeratorForm

        # ���� ��� ������� ���� �� ��������� ������� ��������, �� �������� ������
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    login_url = "/user/login/"
    redirect_field_name = "/"





class ContactListView(ListView):
    model = Contact
