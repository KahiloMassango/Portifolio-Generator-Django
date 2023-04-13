from django.urls import path
from . import views

app_name = 'portifolio'

urlpatterns = [
    path('<slug:slug>', views.home, name='home'),

]
