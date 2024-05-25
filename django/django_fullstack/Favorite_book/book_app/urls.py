from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('Register', views.create),
    path('Login', views.login),
    path('logout', views.logout),
    path('books', views.main),
    path('add', views.add_book),
    path('books/<int:book_id>', views.details),
    path('books/<int:book_id>/edit', views.update),
    path('books/<int:book_id>/favorite', views.favor),
    path('books/<int:book_id>/unfavorite', views.un_favor),
    path('books/<int:book_id>/delete', views.Delete)
]
