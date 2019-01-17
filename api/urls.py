from django.conf.urls import url
from . import views


urlpatterns = [
url(r'jobs/search/(?P<search>.+)', views.search_jobs.as_view(), name = 'jobs'),
url(r'jobs/(?P<pk>\d+)', views.detail_jobs.as_view(), name = 'jobs_detail'),
url(r'jobs/', views.get_jobs.as_view(), name = 'jobs'),


]