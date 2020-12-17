import debug_toolbar
from django.conf import settings
from django.urls import include, path
from . import views


urlpatterns = [
    path('home', views.home, name='SAT_Home'),
    path('practice_test_1', views.test1, name='Practice_Test_1'),
    path('practice_test_2', views.test2, name='Practice_Test_2'),
    path('practice_test_3', views.test3, name='Practice_Test_3'),
    path('practice_test_4', views.test4, name='Practice_Test_4'),
    path('practice_test_5', views.test5, name='Practice_Test_5'),
    path('practice_test_6', views.test6, name='Practice_Test_6'),
    path('final_score', views.final, name='Final_score'),
    path('tips', views.tips, name='Tips & Tricks'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    path('__debug__/', include(debug_toolbar.urls)),
]
