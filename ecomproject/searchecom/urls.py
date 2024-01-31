from django.urls import path
from . import views

app_name='searchecom'
urlpatterns = [
    path('',views.SearchRes,name='SearchRes'),

]