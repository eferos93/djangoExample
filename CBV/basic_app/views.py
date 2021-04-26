from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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


class SchoolCreateView(CreateView):
    # fields you can create
    fields = ('name', 'principal', 'location')
    model = models.School

    # if creation succeeded, go to the returned url
    def get_success_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.object.pk})


class SchoolUpdateView(UpdateView):
    # fields you can modify
    fields = ('name', 'principal')
    model = models.School

    # if modification succeeded, go to the returned link
    def get_success_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.object.pk})


class SchoolDeleteView(DeleteView):
    model = models.School
    # does it in the lazy way, namely once the school is deleted, go back to the given page
    success_url = reverse_lazy('basic_app:list')
