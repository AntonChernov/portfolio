__author__ = 'tito'
from django.conf.urls import patterns, url

from fetr import views

urlpatterns=patterns('',
    url(r'^$', 'fetr.views.all_alb'),
    url(r'^all/(?P<id>\d+)/', 'fetr.views.det_imag'),

)

