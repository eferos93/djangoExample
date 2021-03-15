from django.shortcuts import render
from first_model_app.models import Topic, Webpage, AccessRecord


# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dictionary = {'access_records': webpages_list}
    return render(request, 'first_model_app/index.html', context=date_dictionary)
