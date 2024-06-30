from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import ModelTestForm,AreaForm,ClassForm
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import ModelTest,Category,Area,Class,Group,Report
from .mixins import CommonContextMixin
from django.views.generic import TemplateView


# Create your views here.


#class IndexView(TemplateView):
#   template_name = 'index/index.html'


class ModelListView(CommonContextMixin,ListView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'django_module_basic/model_list.html'  # Specify the template for the list view
    context_object_name = 'model_list'  # Name of the variable to use in the template
    paginate_by = 3  # Display 10 items per page
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['areas'] = Area.objects.all()
        categories = Category.objects.prefetch_related('models')
        context['categories_with_models'] = categories
        return context
    


class ModelDetailView(CommonContextMixin,DetailView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'django_module_basic/model_detail.html'  # Specify the template for the detail view
    context_object_name = 'model'  # Name of the variable to use in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ModelCreateView(CommonContextMixin,CreateView):
    model = ModelTest
    form_class = ModelTestForm
    template_name = 'django_module_basic/model_form.html'
    success_url = reverse_lazy('django_module_basic:model-list')


    

class ModelUpdateView(CommonContextMixin,UpdateView):
    model = ModelTest
    form_class = ModelTestForm
    template_name = 'django_module_basic/model_form.html'
    success_url = reverse_lazy('django_module_basic:model-list')



class ModelDeleteView(CommonContextMixin,DeleteView):
    model = ModelTest
    template_name = 'django_module_basic/model_confirm_delete.html'
    success_url = reverse_lazy('django_module_basic:model-list')

#Area list view
class AreaListView(CommonContextMixin, ListView):
    model = Area
    template_name = 'django_module_basic/area_list.html'
    context_object_name = 'areas'
    paginate_by = 3

class AreaDetailView(CommonContextMixin,DetailView):
    model = Area
    template_name = 'django_module_basic/area_detail.html'
    context_object_name = 'area'

class AreaCreateView(CommonContextMixin,CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'django_module_basic/area_form.html'
    success_url = reverse_lazy('django_module_basic:model-list')

class AreaUpdateView(CommonContextMixin,UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'django_module_basic/area_form.html'
    success_url = reverse_lazy('django_module_basic:model-list')

class AreaDeleteView(CommonContextMixin,DeleteView):
    model = Area
    template_name = 'django_module_basic/area_confirm_delete.html'
    success_url = reverse_lazy('django_module_basic:model-list')


#Class view
class ClassListView(CommonContextMixin, ListView):
    model = Class
    template_name = 'django_module_basic/class_list.html'
    context_object_name = 'classes'
    paginate_by = 3

 

class ClassDetailView(CommonContextMixin, DetailView):
    model = Class
    template_name = 'django_module_basic/class_detail.html'
    context_object_name = 'class'

class ClassCreateView(CommonContextMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'django_module_basic/class_form.html'
    success_url = reverse_lazy('django_module_basic:class-list')

class ClassUpdateView(CommonContextMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'django_module_basic/class_form.html'
    success_url = reverse_lazy('django_module_basic:class-list')

class ClassDeleteView(CommonContextMixin, DeleteView):
    model = Class
    template_name = 'django_module_basic/class_confirm_delete.html'
    success_url = reverse_lazy('django_module_basic:class-list')

#Group view
class GroupListView(CommonContextMixin,ListView):
    model = Group
    template_name = 'django_module_basic/group_list.html'
    context_object_name = 'groups'
    paginate_by = 3



class GroupDetailView(CommonContextMixin,DetailView):
    model = Group
    template_name = 'django_module_basic/group_detail.html'
    context_object_name = 'group'

class GroupCreateView(CommonContextMixin,CreateView):
    model = Group
    fields = ['group_name']
    template_name = 'django_module_basic/group_form.html'
    success_url = reverse_lazy('django_module_basic:group-list')
                                                        
class GroupUpdateView(CommonContextMixin,UpdateView):
    model = Group
    fields = ['group_name']
    template_name = 'django_module_basic/group_form.html'
    success_url = reverse_lazy('django_module_basic:group-list')

class GroupDeleteView(CommonContextMixin,DeleteView):
    model = Group
    template_name = 'django_module_basic/group_confirm_delete.html'
    success_url = reverse_lazy('django_module_basic:group-list')

#Views for the report

class UsersPerAreaView(DetailView):
    model = Area
    template_name = 'django_module_basic/users_per_area.html'
    context_object_name = 'area'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users_by_category = {}
        total_user_count = self.object.users.count()

        # Organize users by category and count them
        for user in self.object.users.all():
            model_tests = ModelTest.objects.filter(first_name=user.first_name)
            for model_test in model_tests:
                category = model_test.category.title
                if category not in users_by_category:
                    users_by_category[category] = {
                        'users': [],
                        'count': 0
                    }
                users_by_category[category]['users'].append((user, model_test.class_model))  # Include class_model here
                users_by_category[category]['count'] += 1

        context['users_by_category'] = users_by_category
        context['total_user_count'] = total_user_count
        return context

class RecordListView(ListView):
    template_name = 'django_module_basic/record_list.html'
    queryset = Report.objects.all()  # Retrieve all ModelTest instances
    context_object_name = 'records'