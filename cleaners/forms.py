from django import forms
from django.forms import widgets
from . import models
from cities.models import City


class CleanerForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        queryset=City.objects.all()
    )

    class Meta:
        model = models.Cleaner
        fields = ['first_name', 'last_name', 'quality_score', 'cities']

