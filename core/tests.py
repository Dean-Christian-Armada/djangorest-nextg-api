from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from core.vars import hostname

import ast

# Create your tests here.

url = hostname+"/o/token/"

class OauthAccessToken(APITestCase):

	# python manage.py dumpdata oauth2_provider.application --indent=4 > core/fixtures/applications_2016_09_20.json
	# python manage.py dumpdata auth.User --indent=4 > core/fixtures/users_2016_09_20.json
	# users is required because it is a foreign key of the applications
	fixtures = ['users_2016_09_20.json', 'applications_2016_09_20.json']

	def setUp(self):
		token = "Basic QnBQZnQ3Q0g3Tm9HOXNiWU44dHAzeTkzT2hSZ0ROZHlGMk8xZFRHVjpCd0tTRm9lMzRzME03eDl5M3hXeVh0TWZPczI0d3Byekk2cjNpdTM5QzBwUVlWVm1KamtScUpPRFVNRGx6RHp5bktROFR2cktuaGJLUUdIeG9pNmV5dnJIM0hYRFQxbTkwc1lJYmdEdlNVdVJrQjZ3eTJ6d2dDWEdRYWYxaEdCbw=="
		_data = "grant_type=password&username=admin&password=pass1234"
		self.client.credentials(HTTP_AUTHORIZATION=token)
		response = self.client.post(url, _data, content_type="application/x-www-form-urlencoded")
		response = response.content # Gets the content of the response
		response = ast.literal_eval(response) # Converts the json to dictionary
		_token = response["access_token"] # this will be the authorization with the access token 
		auth = "Bearer "+_token # The Authorization Header of Oauth
		self.client.credentials(HTTP_AUTHORIZATION=auth)