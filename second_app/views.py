from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help_http(request):
    help_dictionary = {'help_inserts': 'Help Page'}
    return render(request, 'second_app/help.html', help_dictionary)
