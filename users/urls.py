from django.urls import path
from django.views.generic import TemplateView

app_name = 'users'

urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('signup/', __import__('users').views.signup, name='signup'),
]
