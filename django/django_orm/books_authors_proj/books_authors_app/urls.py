from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('Books', views.show_books),
    path('<title>/<int:num>', views.book_desc),
    path('Authors', views.show_author)
]