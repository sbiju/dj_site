from django.conf.urls import url, include
from django.contrib import admin
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    contact_us,
    BlogViewListApi,
    )

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^contact/$', contact_us, name='contact_us'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^api/posts/$', BlogViewListApi.as_view(), name='posts_api'),

]