from django.conf import settings
from django.urls import include, path
from . import views
from .views import TestList

app_name = "SAT"
urlpatterns = [
    path('/home', views.home, name='SAT_Home'),
    path('/tips', views.tips, name='Tips & Tricks'),
    path('/register', views.register, name='Register'),
    path('/TestList', TestList.as_view(), name='TestList'),

    path('/Test/<int:test_id>/Section/Reading/<int:section_id>', views.reading, name='Reading'),
    path('/Test/<int:test_id>/Section/Writing/<int:section_id>', views.writing, name='Writing'),
    path('/Test/<int:test_id>/Section/MathNC/<int:section_id>', views.mathnc, name='MathNC'),
    path('/Test/<int:test_id>/Section/Math/<int:section_id>', views.math, name='Math'),

    path('/Test/<int:test_id>/Section/<int:section_id>/Question/<int:question_id>/', views.detail, name='Question'),
    path('final_score', views.final, name='Final_Score'),

    path('/Test/<int:test_id>/Section/<int:section_id>/Question/<int:question_id>/results/', views.result, name='results'),
    path('/Test/<int:test_id>/Section/<int:section_id>/Question/<int:question_id>/answer/', views.answer, name='answer'),

]

