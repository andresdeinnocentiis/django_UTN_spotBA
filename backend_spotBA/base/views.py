from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from base.models import Product, Category

# Create your views here.

#def index(request):
#    return HttpResponse('Testing OK.')


def base(request):
    params = {}
    params['site_name'] = 'SpotBA'
    return render(request, 'base.html', params)

def index(request):
    params = {}
    params['site_name'] = 'SpotBA'
    categories = Category.objects.all()
    params['categories'] = categories
    return render(request, 'base/index.html', params)

def products(request):
    params = {}
    params['site_name'] = 'SpotBA'
    products = Product.objects.filter(Q(currency="USD"))
    params['products'] = products
    return render(request, 'pages/products.html', params)

def about(request):
    params = {}
    params['site_name'] = 'SpotBA'
    
    return render(request, 'pages/about.html', {})

def contact(request):
    params = {}
    params['site_name'] = 'SpotBA'
    
    return render(request, 'pages/contact.html', params)