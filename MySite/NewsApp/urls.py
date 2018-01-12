from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from NewsApp.models import Articles
from django.conf import settings
from django.conf.urls.static import static
from NewsApp import views

urlpatterns = [
    url(r'^$',views.postsView.as_view(), name="posts"),
    url(r'^(?P<pk>\d+)$', views.postView.as_view(), name='url_post'),
    url(r'^addcomment/(?P<article_id>[0-9]+)$', views.addcomment, name='addcomment'),
]
