from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models


# Create your views here.


# class CBView(View):
#     def get(self, request):
#         return HttpResponse('Class Based Views are cool')
#
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic injection'
        return context

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'  # name of the context dict returned


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # by default, the name of the context dict would be just the model name lower cased
    context_object_name = 'school_detail'
