from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse('Testing OK.')



def index(request):
    params = {}
    params['nombre_sitio'] = 'SpotBA'
    return render(request, 'base/index.html', params)