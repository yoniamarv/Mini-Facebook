from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from profile_app.models import Profile
from django.contrib.auth import authenticate, login, logout
import datetime
import logging


def search(request, value):
    # products = Product.objects.all().filter(name = value)
    # return render(request, 'index.html', context={'products': products})
    pass


def home(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile_info = Profile.objects.get(user=user)

        return render(request, 'home.html', {'logged_in': True, 'picture': user_profile_info.picture.url})
    else:
        return render(request, 'home.html', {'logged_in': False})


def all_users(request):
    if request.user.is_authenticated:
        list_users = Profile.objects.exclude(user=request.user)
        profile_connected_user = Profile.objects.get(user=request.user)
        return render(request, 'all_users.html', context={'list_users': list_users, 'list_people_i_follow': profile_connected_user.follows.all(), 'logged_in': True, 'user': request.user})


@login_required
def follow_user(request, user_id):
    connected_user = request.user
    profile_connected_user = Profile.objects.get(user=connected_user)
    user_to_follow = Profile.objects.get(user__id=user_id)
    profile_connected_user.follows.add(user_to_follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow_user(request, user_id):
    connected_user = request.user
    profile_connected_user = Profile.objects.get(user=connected_user)
    user_to_unfollow = Profile.objects.get(user__id=user_id)
    profile_connected_user.follows.remove(user_to_unfollow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
