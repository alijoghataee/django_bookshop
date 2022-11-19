from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

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
    fields = ['title', 'description', 'author', 'price', 'cover']
    template_name = "books/book_create_view.html"


class UpdateBookView(generic.UpdateView):
    model = Book
    # form_class = BookModelForm
    fields = ['title', 'description', 'author', 'cover']
    template_name = 'books/book_update_view.html'


class DeleteBookView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete_view.html'
    success_url = reverse_lazy('books_list')
