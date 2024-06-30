# report/urls.py
from django.urls import path
from .views import check_in,check_out
app_name= 'report'
urlpatterns = [
    path('check-in/', check_in, name='check-in'),
    path('check-out/', check_out, name='check-out'),
    # Add other paths here
]
