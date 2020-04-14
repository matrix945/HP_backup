from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('movie.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^$', views.index, name='index'),
    # url(r'.*', lambda request: render(request, '404.html'), name='404'),
    # url('admin/', admin.site.urls),
]
