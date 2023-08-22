from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.comment_list, name='home'),
]
