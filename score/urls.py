from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.scores),
    url(r'^get/(?P<score_id>\d+)/$',views.score),
    url(r'^search/$',views.search_title),
]
