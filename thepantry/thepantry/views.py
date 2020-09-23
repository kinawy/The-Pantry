from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def profile(request):
    return render(request)