from api.v1.core.accounts.serializers import LoginAuthenticationSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.accounts.models import UserAccount
from core.methods import standardResponse

from collections import OrderedDict

from oauth2_provider.models import AccessToken

class Login(APIView):
	"""
	Login Authentication
	"""
	throttle_scope = 'login-auth'

	model 				= User
	permission_classes 	= (AllowAny,)
	serializer_class 	= LoginAuthenticationSerializer
		
		
	def post(self, request, *args, **kwargs):
		request_data = request.data

		login_auth = authenticate(username=request_data["username"], password=request_data["password"])

		if login_auth:
			if login_auth.is_active:
				user_account = UserAccount.objects.get(user=login_auth)

				serializer = standardResponse(data=self.serializer_class(user_account).data)

				serializer["data"]["token"] = "Bearer {}".format(AccessToken.objects.get(user=login_auth).token)

				return Response(OrderedDict(serializer), status=status.HTTP_200_OK)
			else:
				return Response(standardResponse(data=request_data, errors="User is inactive"), status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(standardResponse(errors="Wrong username or password"), status=status.HTTP_400_BAD_REQUEST)

login = Login.as_view()