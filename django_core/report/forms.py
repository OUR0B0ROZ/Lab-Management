from django import forms
from django_module_basic.models import Area,Class  # Import the correct model

class CheckInForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), empty_label="Select Area")
    class_model = forms.ModelChoiceField(queryset=Class.objects.all(), label='Class')  # Add this line
    code = forms.CharField(max_length=10)

class CheckOutForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), empty_label="Select Area")
    code = forms.CharField(max_length=10)