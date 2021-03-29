from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.


# class CBView(View):
#     def get(self, request):
#         return HttpResponse('Class Based Views are cool')

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic injection'
        return context
