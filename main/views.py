from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth import login, authenticate
from django.views.generic import View

from customers.forms import CustomerForm
from customers.models import Customer

from bookings.forms import BookingForm

from cleaners.models import Cleaner

from cities.models import City


def home(request):
    return render(request, "main/home.html")


class SignUp(View):

    def post(self, request, *args, **kwargs):
        customerform = CustomerForm(request.POST)
        if customerform.is_valid():
            first_name = customerform.cleaned_data.get('first_name')
            last_name = customerform.cleaned_data.get('last_name')
            phone_number = customerform.cleaned_data.get('phone_number')
            self.date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d %H:%M")
            self.city = customerform.cleaned_data.get('city')
            customer = self.get_customer(first_name, last_name, phone_number)
            cleaner = self.get_cleaner()

            if not cleaner:
                return render(request, 'fail.html', None)

            updated_data = request.POST.copy()
            updated_data.update({
                'customer': customer.id,
                'cleaner': cleaner.id
            })
            booking = BookingForm(updated_data)
            if booking.is_valid():
                booking.save()

                return render(request, 'success.html', {'cleaner': cleaner})
        else:
            context = {
                'form': customerform,
            }
            return render(request, 'signup.html', context)

    def get_customer(self, first_name, last_name, phone_number):
        customer, created = Customer.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        return customer

    def get_cleaner(self):
        cleaner = Cleaner.objects.filter(
            cities__id=self.city.id,
        ).exclude(booking__date=self.date).first()
        return cleaner

    def get(self, request, *args, **kwargs):
        context = {
            'form': CustomerForm,
        }
        return render(request, 'signup.html', context)
