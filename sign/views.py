from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = Person.objects.get(user=self.request.user)
        return context


class PersonUpdateView(UpdateView):
    template_name = 'person_update.html'

    model = Person
    fields = [
        'name',
        'picture',
    ]

    success_url = "/"


class PersonListView(LoginRequiredMixin, TemplateView):
    template_name = 'person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_list'] = Person.objects.exclude(user=self.request.user)
        return context