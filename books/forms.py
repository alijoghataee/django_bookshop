from django.forms import ModelForm

from .models import Book


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'price']
