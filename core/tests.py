from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from core.models import FeatureToggle
from core.vars import token_url, hostname

import ast
import json

# Create your tests here.

url = token_url
url_1 = hostname+"/v1/"

class FeatureToggling(APITestCase):
	fixtures = ['feature_toggle.json']
	def test_get(self):
		# python manage.py dumpdata core.FeatureToggle --indent=4 > core/fixtures/feature_toggle.json
		response = self.client.get(url_1)
		data = json.loads(response.content)["data"]
		self.assertIn("status", data[0]) # Check if there is a "status" key
		self.assertEqual(1, data[0]['status']) # Make sure that only with status true is shown
		self.assertIn("name", data[0]) # Check if there is a "name" key
		self.assertNotEqual(0, len(data[0]['name'])) # Make sure that the value is not empty
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class OauthAccessToken(APITestCase):

	# python manage.py dumpdata oauth2_provider.application --indent=4 > core/fixtures/applications.json
	# python manage.py dumpdata auth.User --indent=4 > core/fixtures/users.json
	# users is required because it is a foreign key of the applications
	fixtures = ['users.json', 'applications.json']

	def setUp(self):
		token = "Basic ZVMyUjVUM2RlSFhNUW0wZWZRcVdiRjE1ekxyT09lSnhqR2xmaWZ4TTpIa2cxOXhta3RsbHBRdjRDRXRkZUFnbXJuSElrYVRGN1BzcTRNYmZIVFpvcll1MkFRMXRQaTJUenI4WFRoTmw1cE5pMU1NYWV1dm9LbGg4YmNzcDJYOGw1SmRiVk1GakhBRGx6RkZMSFFNbG5iTzJWTGxPbkFjTW1aRU01Q2Zsbg=="
		_data = "grant_type=password&username=dean&password=armada13"
		self.client.credentials(HTTP_AUTHORIZATION=token)
		response = self.client.post(url, _data, content_type="application/x-www-form-urlencoded")
		response = response.content # Gets the content of the response
		response = ast.literal_eval(response) # Converts the json to dictionary
		_token = response["access_token"] # this will be the authorization with the access token 
		auth = "Bearer "+_token # The Authorization Header of Oauth
		self.client.credentials(HTTP_AUTHORIZATION=auth)