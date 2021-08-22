from django.urls import path
from django.shortcuts import render, redirect
from .views import *


urlpatterns = [
                path('', index),
                path('authors', authors),
                path('books/<int:book_id>', book),
                path('authors/<int:author_id>', author),
                path('book_add', book_add),
                path('author_add', author_add),
                path('add_author_to_book', add_author_to_book),
                path('add_book_to_author', add_book_to_author)
              ]
