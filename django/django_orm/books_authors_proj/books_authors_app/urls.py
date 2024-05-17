from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('Books', views.show_books),
    path('authors', views.authors),
    path('Authors', views.show_author),
    path('books/id', views.View_Book),
]