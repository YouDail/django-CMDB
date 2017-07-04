from django.conf.urls import url, include
from .views  import *

urlpatterns = [
    url(r'^index$', index),
    url(r'^login$', login),
    url(r'^register$', register),
    url(r'^register_repeat$', register_repeat),
    url(r'^userlist/', userlist)
]