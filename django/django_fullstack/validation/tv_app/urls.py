from django.urls import path

from .import views

urlpatterns = [
    path('shows/new', views.index),
    path('show', views.add),
    path('shows', views.display),
    path('info/<int:id>', views.info ),
    path('Delete/<int:id>', views.delete),
    path('info/<int:id>/edit', views.make_edit),
    path('edit/show/<int:id>', views.edit_show),
    path('',views.red),
] 
