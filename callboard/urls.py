from django.conf.urls import url, include
from django.contrib import admin

from adverts import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]
