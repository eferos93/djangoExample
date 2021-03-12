from django.shortcuts import render

# Create your views here.

def index(request):
    my_dictionary = { 'insert_content': 'Hello I am from first_model_app'}
    return render(request, 'first_model_app/index.html', context=my_dictionary)