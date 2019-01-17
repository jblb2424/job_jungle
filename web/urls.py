from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'home'),
    url(r'^jobs/(?P<pk>\d+)', views.details),
    url(r'^search/', views.search),
]