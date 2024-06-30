from django import forms
from .code_generator import generate_code
from .models import  ModelTest,Area,Class

class ModelTestAdminForm(forms.ModelForm):
    class Meta:
        model = ModelTest
        fields = '__all__'

    code = forms.CharField(
        label='Preview Code',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
        initial=generate_code()
    )


class ModelTestForm(forms.ModelForm):
    class Meta:
        model = ModelTest
        fields = [ 'autor','first_name','last_name','category','group']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['area_of_use']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name']