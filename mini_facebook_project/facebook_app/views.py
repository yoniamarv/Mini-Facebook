from django.shortcuts import render, redirect
from shop_app.models import #Product, Customer, Comment, Maillot, Question, Response, CommentResponse
# from shop_app.forms import CommentForm, QuestionForm, ResponseForm, CommentResponseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import logging


def search(request,value):
	# products = Product.objects.all().filter(name = value)
	# return render(request, 'index.html', context={'products': products})
    pass

def index(request):
	# users = User.objects.all().filter(is_superuser=False)
	# user = None
	
	# if request.user.is_authenticated:
	# 	  user = request.user
	# products = Product.objects.all()
	# return render(request, 'index.html', context={ 'products': products, 'user': user})
    pass