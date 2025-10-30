from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('signup/', views.signup, name='signup'),
]
