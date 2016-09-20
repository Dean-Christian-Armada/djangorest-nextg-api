from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import FeatureToggle
from core.methods import standardResponse

class Login(APIView):
	"""
	**GET** - lists all available features
	"""
	# serializer_class = FeatureTogglingSerializer

	def get(self, request, *args, **kwargs):
		return HttpResponse("dean")
		# _array = FeatureToggle.objects.filter(status=1)
		# serializer = self.serializer_class(_array, many=True)
		# data = serializer.data
		# return Response(standardResponse(data=data), status=status.HTTP_200_OK)
		
login = Login.as_view()