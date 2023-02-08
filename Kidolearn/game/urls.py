from django.contrib import admin
from django.urls import path, include
from game import views 

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('language', views.language, name="language"),
    path('options', views.options, name="options"),
    path('levels/vegetables', views.levelVege, name="levelVege"),
    path('vegetables/level1', views.levelVege1, name="levelVege1"),
    path('level2', views.levelVege2, name="levelVege2"),
]
