from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landingPage'),
    path('rules/<int:rulesIndex>/', views.rules, name='rulesExplained'),
    path('notables/<int:notablesIndex>/', views.notablesDetail, name='notablesDetail'),
    path('notables/', views.notablesList, name='notablesList'),
    path('externalLinks/', views.externalLinks, name='externalLinks'),
]