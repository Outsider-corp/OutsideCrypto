from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'cryptowallet/index.html')


def exchanges(request, exchange_name: int):
    return HttpResponse(f'Choose Exchange...\n{exchange_name}')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found.</h1>')
