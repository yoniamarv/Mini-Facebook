from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from profile_app.models import Profile
from profile_app.forms import SignupForm, LoginForm, ProfileForm, UserForm


def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            password=password,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email')
        )

        user = authenticate(request, username=username, password=password)

        if 'picture' in request.FILES:
            picture = request.FILES['picture']

        Profile.objects.get_or_create(
            user=user,
            bio=request.POST.get('bio'),
            picture=picture
        )

        if user is not None:
            login(request, user)
            return redirect('/facebook_app/')

    return render(request, 'signup.html', context={
        'signup_form': SignupForm(),
        'profile_form': ProfileForm(),
    })


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/facebook_app/')

    return render(request, 'login.html', context={'login_form': LoginForm()})


def logout_auth(request):
    logout(request)
    return redirect('/facebook_app/')


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', context={'user': user})


def list_users(request):
    if request.user.is_authenticated:
        user = request.user
        list_users = Profile.objects.all()

        return render(request, 'list_users.html', {'logged_in': True, 'list_users': list_users})
    else:
        return render(request, 'list_users.html', {'logged_in': False})


def profile(request):
    connected_user = request.user
    profile_connected_user = Profile.objects.get(user=connected_user)
    followers = profile_connected_user.follows.all()

    return render(request, 'profile.html', context={'profile': profile, 'followers': followers})
