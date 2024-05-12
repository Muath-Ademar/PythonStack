from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
]