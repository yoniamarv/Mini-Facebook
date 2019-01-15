from django.urls import path
from . import views

app_name = 'facebook_app'

urlpatterns = [
  path('', views.home, name='home'),
  path('search/<str:value>', views.search, name='search'),
  path('search/', views.home, name='search'),
]