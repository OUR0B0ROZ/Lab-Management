from django.views.generic.base import ContextMixin
from .models import Category, Area, Class, Group

class CommonContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['areas'] = Area.objects.all()
        context['classes'] = Class.objects.all()
        context['groups'] = Group.objects.all()
        return context
