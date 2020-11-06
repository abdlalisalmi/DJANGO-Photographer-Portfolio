from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, views
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from .models import Account



def login(request):
    template_name = 'login.html'

    if request.user.is_authenticated:
        return redirect('homePage')

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login_user(request, user)
            return redirect('homePage')
        return render(request, template_name, {'error': 'The username and password you entered did not match our records. Please double-check and try again.'})

    return render(request, template_name)


@views.login_required(login_url='account:login')
def logout(request):
    if request.method == 'POST':
        logout_user(request)
        return redirect('account:login')
    return redirect('account:login')

