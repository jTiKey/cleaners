from bootstrap3_datetime.widgets import DateTimePicker

from django import forms
from . import models


class CustomerForm(forms.ModelForm):
    date = forms.DateTimeField(
        help_text='example: 2015-11-20 11:11',
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))

    class Meta:
        model = models.Customer
        fields = ('first_name', 'last_name', 'phone_number', 'city', 'date')