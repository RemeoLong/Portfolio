from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='SAT_Home'),
    path('practice_test_1', views.test1, name='Practice_Test_1'),
    path('practice_test_2', views.test2, name='Practice_Test_2'),
    path('practice_test_3', views.test3, name='Practice_Test_3'),
    path('practice_test_4', views.test4, name='Practice_Test_4'),
    path('practice_test_5', views.test5, name='Practice_Test_5'),
    path('practice_test_6', views.test6, name='Practice_Test_6'),
    path('practice_test_7', views.test7, name='Practice_Test_7'),
    path('practice_test_8', views.test8, name='Practice_Test_8'),
    path('final_score', views.final, name='Final_score'),
    path('tips', views.tips, name='Tips & Tricks'),
]
