from django.urls import path
from . import views


urlpatterns = [
    path('', views.comment_list, name=''),
    path('con', views.con, name='con'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
