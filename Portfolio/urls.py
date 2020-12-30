from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.about, name='Home'),
    path('Experience', views.work, name='Experience'),
    path('II', views.ii, name='II'),
    path('Projects', views.projects, name='Projects'),
    path('About', views.about, name='About'),
    path('new', views.new, name='Back'),
    path('SAT', include('SAT.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
