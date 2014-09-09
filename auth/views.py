# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from auth.forms import RegisterForm, LoginForm
from django.core.context_processors import csrf

# Create your views here.

def logins(request):
    args = {'login': LoginForm()}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request,'auth/login.html', args)
    else:
        return render(request, 'auth/login.html', args)

def register(request):
    args = {'reg': RegisterForm()}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'auth/register.html', args)

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')