from django.shortcuts import render, redirect
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
    Author.objects.create(first_name=request.POST['author_first_name'],
                          last_name=request.POST['author_last_name'],
                          notes=request.POST['author_notes']
                         )
    return redirect('/authors')


def book_add(request):
    Book.objects.create(title=request.POST['book_title'],
                        desc=request.POST['book_description']
                       )
    return redirect('/')


def add_author_to_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['add_author'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')


def add_book_to_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['add_book'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')
