from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import Http404

from .models import Booking
from .forms import BookingForm

# Create your views here.
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        # Only return the current user's bookings
        return Booking.objects.filter(user=self.request.user).order_by("date")


class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Booking
    template_name = "bookings/booking_detail.html"
    context_object_name = "booking"

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user

    def get(self, request, *args, **kwargs):
        """If the booking doesn't exist, redirect to booking list with a friendly message."""
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(request, "No booking found matching the query. You can create a new booking.")
            return redirect('bookings:booking_list')


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = "bookings/create_booking.html"
    form_class = BookingForm
    success_url = reverse_lazy("bookings:booking_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = "bookings/create_booking.html"
    form_class = BookingForm

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user

    def get_success_url(self):
        return reverse_lazy("bookings:booking_detail", kwargs={"pk": self.object.pk})


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "bookings/booking_delete.html"
    success_url = reverse_lazy("bookings:booking_list")

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user


from django.views.generic import TemplateView

class BookingSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "bookings/success.html"



