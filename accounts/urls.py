from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.custom_login, name='login'),
    path("register", views.register_view, name="register"),
    path('create_user', views.register_create, name='register_create'),

]
