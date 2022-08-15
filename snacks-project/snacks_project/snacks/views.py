from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Snacks


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class SnacksList(ListView):
    template_name = "snacks_list.html"
    model = Snacks
    context_object_name = 'sn_list'


class SnacksDetail(DetailView):
    template_name = "snacks_list.html"
    model = Snacks
