from django.conf.urls import url, include
from . import views

def test(request):
    print "*********************"

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]