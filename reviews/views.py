from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review


class ReviewListView(ListView):
	model = Review
	template_name = 'reviews/review_list.html'
	context_object_name = 'reviews'


class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['rating', 'comment', 'image']
	template_name = 'reviews/review_form.html'
	success_url = reverse_lazy('reviews:review_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
