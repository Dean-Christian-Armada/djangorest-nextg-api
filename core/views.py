from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from core.methods import standardResponse, pagination

class FeatureToggling(APIView):
	"""
	**GET** - lists all Albums
	"""
	# serializer_class = AlbumSerializer

	def get(self, request, *args, **kwargs):
		return Response(status=status.HTTP_200_OK)
		# page = request.GET.get('page', None)
		# c = 'albums'
		# if cache.get(c):
		# 	_array = cache.get(c)
		# else:
		# 	_array = Album.objects.filter()
		# 	cache.set(c, _array)
		# if page:
		# 	x = pagination(page)
		# 	_array = _array[x[0]:x[1]]
		# cs = 'albumserializer'
		# if cache.get(cs): # THIS CACHE IS NOT REALLY RECOMMENDED ESPECIALLY IF FILTERS AND SORTING TAKES PLACE
		# 	# print cache.get(cs)
		# 	data = cache.get(cs)
		# 	if page:
		# 		data  = data[x[0]:x[1]]
		# else:
		# 	serializer = self.serializer_class(_array, many=True)
		# 	data = serializer.data
		# 	cache.set(cs, data)
		# if data:
		# 	_status = status.HTTP_200_OK
		# else:
		# 	_status = status.HTTP_204_NO_CONTENT
		# return Response(standardResponse(data=data), status=_status)
feature_toggling = FeatureToggling.as_view()