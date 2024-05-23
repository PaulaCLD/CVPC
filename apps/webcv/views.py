from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProfesionalCV


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = ProfesionalCV.objects.first()
        return context

