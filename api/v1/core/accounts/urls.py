from django.conf.urls import url, include
from django.http import HttpResponse

from api.v1.core.accounts import views

urlpatterns = [
	url(r'login/', views.login, name='login'),
]