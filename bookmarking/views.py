from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookmarking.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 1


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url',]
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', ]
    # success_url = reverse_lazy('list')
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')