from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from oauth2_provider.models import Application, AccessToken

from core.models import FeatureToggle
from core.vars import token_url, hostname

from requests.auth import HTTPBasicAuth

import ast
import json
import requests

# Create your tests here.

url = token_url
url_1 = hostname+"/v1/"

class FeatureToggling(APITestCase):
	fixtures = ['feature_toggle.json']
	def test_get(self):
		# python manage.py dumpdata core.FeatureToggle --indent=4 > core/fixtures/feature_toggle.json
		response = self.client.get(url_1) # client makes a get request
		data = json.loads(response.content)["data"] # backend responses the API
		d_0 = data[0]
		self.assertIn("status", d_0) # Check if there is a "status" key on the API
		self.assertEqual(1, d_0['status']) # Make sure that only with status true is shown on the API
		self.assertIn("name", d_0) # Check if there is a "name" key on the API
		self.assertNotEqual(0, len(d_0['name'])) # Make sure that the value is not empty on the API
		self.assertEqual(response.status_code, status.HTTP_200_OK) # Checks if the API has the right status of 200 OK

# Reusable class to set the UserAccount
class SetUserAccount(APITestCase):
	# python manage.py dumpdata accounts.UserType --indent=4 > core/accounts/fixtures/user_types.json
	# python manage.py dumpdata accounts.UserAccount --indent=4 > core/accounts/fixtures/user_accounts.json
	# python manage.py dumpdata core.School --indent=4 > core/fixtures/schools.json
	# python manage.py dumpdata core.AUState --indent=4 > core/fixtures/au_states.json
	# python manage.py dumpdata core.Course --indent=4 > core/fixtures/courses.json
	# python manage.py dumpdata core.SchoolsAndCourses --indent=4 > core/fixtures/schools_and_courses.json
	# python manage.py dumpdata accounts.UsersAndCourses --indent=4 > core/accounts/fixtures/users_and_courses.json
	fixtures = ['user_types.json', 'au_states.json', 'schools.json', 'user_accounts.json', 'courses.json', 'schools_and_courses.json', 'users_and_courses.json']
	# TODO transfer users_and_courses and courses.json to log-in

# Reusable class to set the token
class OauthAccessToken(APITestCase):

	# python manage.py dumpdata oauth2_provider.application --indent=4 > core/fixtures/applications.json
	# python manage.py dumpdata auth.User --indent=4 > core/fixtures/users.json
	# users is required because it is a foreign key of the applications
	# python manage.py dumpdata oauth2_provider.AccessToken --indent=4 > core/fixtures/access_tokens.json
	fixtures = ['users.json', 'applications.json', 'access_tokens.json']

	def setUp(self):
		app = Application.objects.latest('id') # Get an application
		_token = AccessToken.objects.get(application=app).token # Get the access token of the application
		auth = "Bearer "+_token # The Authorization Header of Oauth
		self.client.credentials(HTTP_AUTHORIZATION=auth) # client sets the authorization header oauth