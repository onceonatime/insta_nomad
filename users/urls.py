from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^explore/$', views.ExploreUsers.as_view(), name='explore_user'),
    url(r'^(?P<user_id>\d+)/follow/$', views.FollowUser.as_view(), name='follow_user'),
    url(r'^(?P<user_id>\d+)/unfollow/$', views.UnFollowUser.as_view(), name='unfollow_user'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^(?P<username>\w+)/$', views.UserProfile.as_view(), name='user_profile'),
    url(r'^(?P<username>\w+)/followers/$', views.UserFollowers.as_view(), name='user_followers'),
    url(r'^(?P<username>\w+)/following/$', views.UserFollowing.as_view(), name='user_following'),
    url(r'^(?P<username>\w+)/password/$', views.ChangePassword.as_view(), name='change_password'),

    url(r'^login/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
]
