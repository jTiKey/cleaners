from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from . import models


class CityList(ListView):
    model = models.City


class CityDetail(DetailView):
    model = models.City


class CityCreation(CreateView):
    model = models.City
    success_url = reverse_lazy('cities:list')
    fields = ['name', ]


class CityUpdate(UpdateView):
    model = models.City
    success_url = reverse_lazy('cities:list')
    fields = ['name', ]


class CityDelete(DeleteView):
    model = models.City
    success_url = reverse_lazy('cities:list')