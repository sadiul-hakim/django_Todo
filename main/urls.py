from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from .CustomAuthenticationForm import CustomAuthenticationForm

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(
        template_name="main/login.html",
        authentication_form=CustomAuthenticationForm,
        redirect_authenticated_user=True
    ),
        name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/<int:id>", views.delete_todo, name="delete"),
    path("edit/<int:id>", views.edit_view, name="edit"),
    path('search/', views.search_todo, name="search")
]
