from django.contrib import admin
from django.urls import path, include

from .views import homePage

urlpatterns = [
    path('', homePage, name = 'homePage'),

    path('', include('account.urls')),

    path('admin/', admin.site.urls),
]
