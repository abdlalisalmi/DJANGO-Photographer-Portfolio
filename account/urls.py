from django.urls import path
from .views import (
    login,
    logout,
)


app_name = 'account'
urlpatterns = [
    path('login/', login, name='login'),
    path('admin/login/', login),
    path('logout/', logout, name='logout'),
]
