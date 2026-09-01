from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("delete/<int:id>", views.delete_todo, name="delete"),
    path("edit/<int:id>", views.edit_view, name="edit"),
    path('search/', views.search_todo, name="search")
]
