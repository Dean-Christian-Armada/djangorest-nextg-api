from django.conf.urls import url, include
from django.http import HttpResponse

from core.accounts import views

urlpatterns = [
 	url(r'^', views.login),
]