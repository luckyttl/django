# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def index(request):
    return render(request,'app/index.html')

def login_page(request):
    if request.method=='GET':
        return render(request,'app/login.html')
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
    user=authenticate(username=username,password=password)
    if user:
        login(request,user)
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/login')

