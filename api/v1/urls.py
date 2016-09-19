from django.conf.urls import url, include
from django.http import HttpResponse

from core.views import feature_toggling

urlpatterns = [
	# url(r'^artists/', include('api.v1.store.artists.urls'), name="dean"),
 	# url(r'^', include('api.v1.store.urls')),
 	url(r'^', feature_toggling),
 	url(r'^docs/', include('rest_framework_docs.urls')),
 	# /api/v1/docs/
]