# ice_cream/urls.py
from django.urls import path

from . import views
app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index,name = 'posts_main'),
    # Страница со списком сортов мороженого
    path('group_list.html', views.group_posts,name = 'posts_group'),
] 