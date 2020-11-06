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

    # path('profile/', profile, name='profile'),
    # path('settings/', settings, name='settings'),

    # path('search/', search, name='search'),
    # path('account/<str:account>/', profile_visit, name='profile_visit'),

]
