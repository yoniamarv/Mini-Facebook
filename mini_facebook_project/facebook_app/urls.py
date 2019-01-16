from django.urls import path
from . import views

app_name = 'facebook_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('all_users/', views.all_users, name='all_users'),
    path('follow/<int:user_id>', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>', views.unfollow_user, name='unfollow'),
    #path('search/<str:value>', views.search, name='search'),
    #path('search/', views.home, name='search'),
]
