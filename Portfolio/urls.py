from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.about, name='Home'),
    path('Experience', views.work, name='Experience'),
    path('Projects', views.projects, name='Projects'),
    path('About', views.about, name='About'),
    path('SAT', include('SAT.urls')),
]
