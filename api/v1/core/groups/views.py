from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.methods import standardResponse

class GroupList(APIView):		
	def get(self, request, *args, **kwargs):
		return Response(standardResponse(data="Hello World"), status=status.HTTP_200_OK)
group_list = GroupList.as_view()