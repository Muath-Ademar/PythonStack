from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('Books', views.show_books),
    path('authors', views.authors),
    path('Authors', views.show_author),
    path('books/<int:id>', views.View_Book, name= "book"),
    path('authors/<int:id>', views.View_author, name = "author"),
    path('display_authors',  views.display_authors),
]