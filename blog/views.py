from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView, CreateView, DetailView, UpdateView
from pytils.translit import slugify

from blog.models import Blogpost
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin, ListView):
    model = Blogpost


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blogpost
    fields = ('name', 'text', 'image', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blogpost
    fields = ('name', 'text', 'image', 'is_published')

    def get_success_url(self):
        agent_id = self.object.id
        return reverse_lazy('blog:detail_post', kwargs={'pk': agent_id})


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

