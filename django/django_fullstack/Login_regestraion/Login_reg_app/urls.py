from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Register', views.create),
    path('Login', views.login),
    path('success', views.success),
    path("logout", views.logout),

]
