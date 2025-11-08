from django import forms
from django.forms import widgets
from django.forms.widgets import SplitDateTimeWidget
from .models import Booking, BookingImage


class BookingForm(forms.ModelForm):
    # Use a SplitDateTimeField so the form expects two inputs (date + time)
    date = forms.SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'}, time_attrs={'type': 'time'}
        )
    )

    class Meta:
        model = Booking
        fields = ['restaurant', 'date', 'guests', 'special_requests']


class BookingImageForm(forms.ModelForm):
    class Meta:
        model = BookingImage
        fields = ['image']
