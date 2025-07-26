from django.urls import re_path

from . import views


urlpatterns = [
    re_path('^main/', views.main, name='main_menu_page'),
]
