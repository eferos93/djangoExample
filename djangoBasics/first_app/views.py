from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # the key must refer to a template tag
    my_dictionary = {'insert_me': 'Hello I am from first_app/index.html'}
    return render(request, 'first_app/index.html', context=my_dictionary)
