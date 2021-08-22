from django.shortcuts import render
from .models import *


def index(request):
    context = {
                'books': Book.objects.all(),
              }
    return render(request, 'index.html', context)


def authors(request):
    context = {
                'authors': Author.objects.all()
              }
    return render(request, 'authors.html', context)


def author(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "books": Book.objects.all()
    }
    return render(request, 'author.html', context)


def book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "authors": Author.objects.all()
    }
    return render(request, 'book.html', context)


def author_add(request):
    pass


def book_add(request):
    pass


def add_author_to_book(request):
    pass


def add_book_to_author(request):
    pass
