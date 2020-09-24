from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from .forms import SignUpForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


def login_view(request):
    # if post then authenticate(user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled')
            else:
                print('The username and/or password is incorrect.')

        else:
            return render(request, 'login.html', {'form': form})
    else:  # it was a get request so send the empty login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/user/'+str(user.username))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    post = Post.objects.filter(user=user)
    return render(request, 'profile.html', { 'username':username })


def signup(request):
    return render(request, 'signup.html')


def login_page(request):
    return render(request, 'login.html')

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    fields = ['category', 'itemName', 'weightQuantity', 'description']

    def form_valid(self, form):
        # This lets us catch the PK, if we didn't do this we'd have no way of accessing this pk from this CRUD right here
        self.object = form.save(commit=False) # Don't post to DB until I say so, this is the form validation
        self.object.user = self.request.user
        user = self.object.user
        self.object.save() # This gives us access to the PK thhrough the self.object
        return HttpResponseRedirect('/user/'+str(user.username))
