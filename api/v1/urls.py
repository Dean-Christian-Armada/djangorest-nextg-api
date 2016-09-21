from django.conf.urls import url, include
from django.http import HttpResponse

# from core import views

urlpatterns = [
 	url(r'^', include('api.v1.core.urls')),
 	url(r'^docs/', include('rest_framework_docs.urls')),
 	url(r'^accounts/', include('api.v1.core.accounts.urls')),
 	url(r'^students/', include('api.v1.students.urls')),
]