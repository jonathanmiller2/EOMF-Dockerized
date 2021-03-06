#TODO: Are these imports needed?
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from django.urls import re_path
import ceom.feedback.views

urlpatterns = [
        re_path(r'^ajax(?P<url>.*)$', ceom.feedback.views.handle_ajax),
        re_path(r'^tracking/$', ceom.feedback.views.feedback_details),
        re_path(r'^comment/(?P<id>[0-9]+)', ceom.feedback.views.comment_page),
]

# vim: et sw=4 sts=4
