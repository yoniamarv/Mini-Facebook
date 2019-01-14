from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from profile_app.models import UserProfileInfo
from profile_app.forms import SignupForm, LoginForm, ProfileForm, UserForm, ProfileForm


def index(request):
    pass

def signup(request):
  if request.method == 'POST':
    User.objects.create_user(
      username=request.POST.get('username'),
      password=request.POST.get('password'),
      first_name=request.POST.get('first_name'),
      last_name=request.POST.get('last_name'),
      email=request.POST.get('email'),
    )

    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

    Profile.objects.get_or_create(
      user=user,
      bio='',
      gender=Gender.objects.get(id=request.POST.get('gender')),
      picture=Picture.objects.get(id=request.POST.get('picture')),
    )

    if user is not None:
      login(request, user)
      return redirect('/profile_app/')

  return render(request, 'signup.html', context={
      'signup_form': SignupForm(),
      'extra_info_form': ExtraInfoForm(),
    })

def login_auth(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/profile_app/')

def logout_auth(request):
  logout(request)
  return redirect('/profile_app/')


def profile(request, user_id):
  user = User.objects.get(id=user_id)
  return render(request, 'profile.html', context={ 'user': user })