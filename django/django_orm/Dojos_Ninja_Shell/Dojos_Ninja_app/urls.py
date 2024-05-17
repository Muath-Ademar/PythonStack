from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_dojo', views.show_dojo),
    path('add_ninja', views.show_ninja)  
]