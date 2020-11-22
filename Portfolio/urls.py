from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('Contact', views.contact, name='Contact'),
    path('Experience', views.work, name='Experience'),
    path('Projects', views.projects, name='Projects'),
    path('About', views.about, name='About Me'),
]
