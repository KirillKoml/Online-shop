from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from blog.models import Blog

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "description", "image", "data_bd")
    success_url = reverse_lazy('Blog:Blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("name", "description", "image", "data_bd")
    success_url = reverse_lazy('Blog:Blog_list')

    def get_success_url(self):
        return reverse('Blog:Blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('Blog:Blog_list')


