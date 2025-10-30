from django.urls import path
from .views import ReviewListView, ReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
]
