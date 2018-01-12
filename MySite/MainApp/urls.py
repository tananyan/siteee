from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^news/', include('NewsApp.urls')),
    url(r'^contact/$', views.contact.as_view(), name='contact'),
    url(r'^registration/$', views.registration.as_view(), name='registration'), #S
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]