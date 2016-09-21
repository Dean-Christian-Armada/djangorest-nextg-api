from api.v1.core.accounts.serializers import LoginAuthenticationSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import FeatureToggle
from core.methods import standardResponse

from core.accounts.models import UserAccount

from oauth2_provider.models import AccessToken

class Login(APIView):
	"""
	Login Authentication
	"""
	model 				= User
	permission_classes 	= (AllowAny,)
	serializer_class 	= LoginAuthenticationSerializer
	# queryset            = User.objects.all()

	def get(self, request, *args, **kwargs):
		return HttpResponse("get")
		# _array = FeatureToggle.objects.filter(status=1)
		# serializer = self.serializer_class(_array, many=True)
		# data = serializer.data
		# return Response(standardResponse(data=data), status=status.HTTP_200_OK)
		
		
	def post(self, request, *args, **kwargs):
		request_data = request.data

		login_auth = authenticate(username=request_data["username"], password=request_data["password"])

		if login_auth:
			if login_auth.is_active:
				user_account = UserAccount.objects.get(user=login_auth)

				serializer = self.serializer_class(user_account)

				# serializer.data["token"] = "Bearer {}".format(AccessToken.objects.get(user=login_auth).token)

				return Response(standardResponse(data=serializer.data), status=status.HTTP_200_OK)
			else:
				return Response(standardResponse(data=request_data, errors="User is inactive"), status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(standardResponse(data=request_data, errors="Wrong username or password"), status=status.HTTP_400_BAD_REQUEST)

login = Login.as_view()