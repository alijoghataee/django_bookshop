from django.shortcuts import render
from django.views import generic

from .models import Book
from .forms import BookModelForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list_view.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/books_detail_view.html'


class BookCreateView(generic.CreateView):
    # form_class = BookModelForm
    model = Book
    fields = ['title', 'description', 'author', 'price']
    template_name = "books/create_view.html"

