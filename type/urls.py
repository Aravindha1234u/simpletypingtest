from django.urls import path
import type.views as views

urlpatterns = [
    path('',views.index,name="index"),
    path('words',views.randomwords,name="randomwords"),
]
