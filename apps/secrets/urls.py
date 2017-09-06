from django.conf.urls import url
from . import views

def test(request):
    print "*********************"

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^delete_secret$', views.delete_secret, name = 'delete_secret'),
    url(r'^like_secret$', views.like_secret, name = 'like_secret'),
    url(r'^logout$', views.logout, name = 'logout'),
]