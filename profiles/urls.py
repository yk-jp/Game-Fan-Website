from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landingPage'),
    path('rules/<int:rulesIndex>/', views.rules, name='rulesExplained'),
    path('notables/<int:notablesIndex>/', views.notablesList, name='notablesList'),
    path('notables/<int:notablesIndex>/<int:notableIndex>/', views.notablesDetail, name='notablesDetail'),
    path('externalLinks/', views.externalLinks, name='externalLinks'),
]