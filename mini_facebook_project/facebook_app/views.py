from django.shortcuts import render, redirect
# from shop_app.forms import CommentForm, QuestionForm, ResponseForm, CommentResponseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import logging
from profile_app.models import Profile 


def search(request,value):
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

   