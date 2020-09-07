from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import create


app_name='createPost'
urlpatterns = [
    path('', create.as_view(),name='create'),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns +=staticfiles_urlpatterns()
