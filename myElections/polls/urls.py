from django.urls import path, include
from . import views
from django.urls import re_path

"""
This file contains all the URLs of the elections site run by the polls app.

:param str app_name: The name of the app that will be referred to.
:param lst urlpatterns: Stores all the URL paths that are called in the polls app.
"""

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/', views.poll, name='poll'),
    path('about/', views.about, name='about'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]

