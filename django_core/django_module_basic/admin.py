from django.contrib import admin
from .models import Category, ModelTest,Area,Group,Class
from .code_generator import generate_code
from .forms import  ModelTestAdminForm 
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ModelTest)
class ModelTestAdmin(admin.ModelAdmin):
    form = ModelTestAdminForm  # Use the custom form
    list_display = ['first_name', 'code', 'created']  # Include 'code' in the list display
    prepopulated_fields = {'slug': ('first_name',)}


    def save_model(self, request, obj, form, change):
        if not obj.code:
            obj.code = generate_code()
        super().save_model(request, obj, form, change)

admin.site.register(Area)
admin.site.register(Class)
admin.site.register(Group)
