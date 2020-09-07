from django.urls import path,include
from django.conf.urls import url
from . import views
from .views import index,show,cat,categ


app_name='blog'
urlpatterns = [
    path('', index.as_view(),name='index'),
    path('category', cat.as_view(),name='category'),
    url(r'^category/(?P<test>[a-z]+[0-9]+)/$', categ.as_view()),
    url(r'^post/(?P<id>[0-9]+)/$',show.as_view(),name='show'),

]
