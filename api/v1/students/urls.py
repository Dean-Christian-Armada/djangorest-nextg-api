from django.conf.urls import url, include
from django.http import HttpResponse

from api.v1.students import views

urlpatterns = [
 	url(r'(?P<user_account_id>[0-9]+)/units/', views.units_list, name='students-units-list'),
]