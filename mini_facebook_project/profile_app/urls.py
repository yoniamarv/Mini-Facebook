from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_auth, name='login'),
  path('logout/', views.logout_auth, name='logout'),
]