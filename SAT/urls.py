from django.conf import settings
from django.urls import include, path
from . import views
from .views import TestList

app_name = "SAT"
urlpatterns = [
    path('/home', views.home, name='SAT_Home'),
    path('/tips', views.tips, name='Tips & Tricks'),
    path('/register', views.register, name='Register'),
    path('/Tests', TestList.as_view(), name='TestList'),
    path('/Tests/<int:test_id>', views.test, name='Test'),
    path('/Tests/<int:test_id>/Sections/<int:section_id>', views.sections, name='Section'),
    path('/Test/<int:test_id>/Sections/<int:section_id>/Question/<int:question_id>/',
         views.detail, name='Question'),

    path('/Test/<int:test_id>/Sections/<int:section_id>/Question/<int:question_id>/answer/',
         views.answer, name='answer'),

    path('/Test/<int:test_id>/Sections/<int:section_id>/Question/<int:question_id>/results/',
         views.result, name='results'),

    path('final_score', views.final, name='Final_Score'),

]


