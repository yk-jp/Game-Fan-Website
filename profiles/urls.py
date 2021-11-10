from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='landingPage'),
    path('rules', views.rules, name='ruleExplained'),
    path('notables', views.notablesDetail, name='notablesDetail'),
    path('notables', views.notablesList, name='notablesList'),
    path('externalLinks', views.externalLinks, name='externalLinks'),
]