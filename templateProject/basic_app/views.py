from django.shortcuts import render


# Create your views here.

def index(request):
    context_dictionary = {'text': 'Hello world!', 'number': 25}
    return render(request, 'basic_app/index.html', context=context_dictionary)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
