
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('list_things.urls')),
    path('admin/', admin.site.urls),
]
