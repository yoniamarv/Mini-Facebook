from django.urls import path
from . import views

app_name = 'facebook_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('search/<str:value>', views.search, name='search'),
  path('search/', views.index, name='search'),
]