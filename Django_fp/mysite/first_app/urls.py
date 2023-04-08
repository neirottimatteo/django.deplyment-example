from django.urls import path
from . import views

app_name='first_app' #used in the html to find this page

urlpatterns = [
    path('index/', views.index,name='index'),
    path('forms/', views.form_name_view,name='forms'),
    path('relative/', views.relative,name='relative'),
    path('other/', views.other,name='other'),

]
