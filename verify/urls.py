from django.urls import path, include
from .views import home, view_cotes
app_name = 'verify'
urlpatterns = [
    path('',home,  name="home"),
    path('mescotes/',view_cotes,  name="search"),
]