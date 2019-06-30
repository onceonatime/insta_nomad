from django.conf.urls import url

from notifications import views

app_name = 'notifications'

urlpatterns = [
    url(r'^$', views.Notifications.as_view(), name='notifications'),
]