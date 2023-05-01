from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    sort_item = request.GET.get('sort', '')
    if sort_item == 'name':
        phones_objects = Phone.objects.order_by('name')
    elif sort_item == 'min_price':
        phones_objects = Phone.objects.order_by('price')
    elif sort_item == 'max_price':
        phones_objects = Phone.objects.order_by('-price')
    context = {
        'phones': phones_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    prod = Phone.objects.get(slug=slug)
    context = {
        'phone': prod
    }
    return render(request, template, context)
