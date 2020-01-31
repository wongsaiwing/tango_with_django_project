from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict={}
    context_dict['boldmessage'] = 'Chunchy, creamy, cookie, candy, cupcake!'
    context_dict['category'] = category_list

    return render(request, 'rango/index.html', context=context_dict)
    #context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return render(request, 'rango/index.html', context=context_dict)
    
# Create your views here.
