from django.urls import path, include
from . import views
# from django.urls import re_path

"""
This file contains all the URLs of the elections site run by the user_auth app.

:param str app_name: The name of the app that will be referred to.
:param lst urlpatterns: Stores all the URL paths that are called in the user_auth app.
"""

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
        name='authenticate_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout')
]

