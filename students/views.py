from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from core.accounts.models import UsersAndUnits
from core.methods import standardResponse
from api.v1.students.serializers import UnitsAndUsersSerializer

class UnitsList(APIView):
	"""
	**GET** - lists all available units
	"""
	serializer_class = UnitsAndUsersSerializer
	# permission_classes = (AllowAny,)

	def get(self, request, *args, **kwargs):
		id_1 = kwargs['user_account_id']
		_array = UsersAndUnits.objects.filter(user_account_id=id_1)
		serializer = self.serializer_class(_array, many=True)
		data = serializer.data
		if data:
			_status = status.HTTP_200_OK
		else:
			_status = status.HTTP_204_NO_CONTENT
		return Response(standardResponse(data=data), status=_status)
		
units_list = UnitsList.as_view()