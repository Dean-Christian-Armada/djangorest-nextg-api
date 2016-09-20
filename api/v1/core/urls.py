from django.conf.urls import url, include
from django.http import HttpResponse

from core import views

urlpatterns = [
 	url(r'^$', views.feature_toggling),
]