from django.shortcuts import render
import json
from books.models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    pub_d = request.GET.get('pub_date')
    # with open('books.json', 'rt', encoding='utf8') as f:
    #     data = json.load(f)
    #     for d in data:
    #         book = Book(
    #         name = d['name'],
    #         author = d['author'],
    #         pub_date = d['pub_date'],
    #         )
    #     book.save()
    # books = Book.objects.all().filter(pub_d)
    try:
        pub_d = datetime.datetime.strptime(pub_d, '%Y-%m-%d')
        context = {
            'books': Book.objects.filter(pub_date__exact=pub_d).order_by('pub_date')
        }
    except TypeError:
        context = {
            'books': Book.objects.order_by('pub_date').all()
        }
    # context = {
    #     'books': books
    # }
    return render(request, template, context)
