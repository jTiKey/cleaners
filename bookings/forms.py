from django import forms
from django.forms import widgets
from . import models


class BookingForm(forms.ModelForm):

    class Meta:
        model = models.Booking
        fields = ('date', 'customer', 'cleaner')

