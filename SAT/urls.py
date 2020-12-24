from django.conf import settings
from django.urls import include, path
from . import views
from .views import TestListView

urlpatterns = [
    path('home', views.home, name='SAT_Home'),
    path('tips', views.tips, name='Tips & Tricks'),
    path('register', views.register, name='Register'),
    path('Test', views.test, name='Test'),
    path('Test/<int:test_id>/', views.quiz, name='TestNum'),
    path('Test/<int:test_id>/Section', views.section, name='Section'),

    path('Test/<int:test_id>/Section/Reading', views.reading, name='Reading'),
    path('Test/<int:test_id>/Section/Writing', views.writing, name='Writing'),
    path('Test/<int:test_id>/Section/MathNC', views.mathnc, name='MathNC'),
    path('Test/<int:test_id>/Section/Math', views.math, name='Math'),

    path('Test/<int:test_id>/Section/<int:section_id>/', views.sect, name='SectionNum'),
    path('Test/<int:test_id>/Section/<int:section_id>/Question/<int:question_id>/', views.detail, name='Question'),
    path('final_score', views.final, name='Final_Score'),

    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),


#    path('Test', TestListView.as_view(), name='Test'),
   path('Test/<int:test_id>/', TestListView.as_view(), name='TestNum'),
#  path('Test/<int:test_id>[1-6]+/Math/<int:section_id>[1-6]+/Question/<int:question_id>/', views., name=''),
#  path('<int:question_id>/', views.detail, name='detail'),


]
