from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import MenuCategory, MenuItem

class MenuListView(ListView):
    template_name = 'menu/menu_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        # Return active items; categories will be fetched in context
        return MenuItem.objects.filter(is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = MenuCategory.objects.prefetch_related('items')
        return ctx


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'menu/menu_item_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
