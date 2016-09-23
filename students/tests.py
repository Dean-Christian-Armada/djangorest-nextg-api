from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from unittest import skip # This library is used to skip some class TestCase

from core.tests import OauthAccessToken, SetUserAccount
 
import time # This library is used in case you want to put a sleep before proceeding to the next line of scripts
import inspect # This library is used to print the method of that certain class.. inspect.stack()[0][3]
import json # This library is for parsing the response.content

# Create your tests here.

url_1 = reverse('students-units-list', kwargs={'user_account_id':8}) # The URL endpoint for the units of students which is /students/8/units/ having GET methods

# # Reusabality Class
# class StudentRecordSetupMixing():
# 	# For reusable of adding a single record
# 	# To be used for POST, GET(detailed), PUT and DELETE
# 	def _setup_add_record(self):
# 		OauthAccessToken.setUp(self) # This is declared to insert the Oauth without interrupting anything from the children classes
# 		_data = {"name": "50 Cent", "birth_date":"2005-02-13"}
# 		response = self.client.post(url_1, _data)
# 		data = json.loads(response.content)["data"]
# 		return ( response, _data, data )

# _cls = StudentRecordSetupMixing # Variable for the re-usable class

class StudentUnitsTestWithoutData(OauthAccessToken):
	fixtures = list(OauthAccessToken.fixtures) # "list" is needed so the addressing of fixtures is different 
	fixtures += SetUserAccount.fixtures
	def test_get(self):
		response = self.client.get(url_1) # client makes a get request
		self.assertEqual(response.content, "")  # Checks if there is a data content
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # Checks if the API has the right status of 204 CREATED

# Check the response if there is given data
class StudentUnitsTestWithData(OauthAccessToken):
	fixtures = list(OauthAccessToken.fixtures) # "list" is needed so the addressing of fixtures is different
	fixtures += SetUserAccount.fixtures
	# python manage.py dumpdata core.Unit --indent=4 > core/fixtures/units.json
	# python manage.py dumpdata accounts.UsersAndUnits --indent=4 > core/accounts/fixtures/users_and_units.json
	# python manage.py dumpdata core.CoursesAndUnits --indent=4 > core/fixtures/courses_and_units.json
	fixtures += ['units.json', 'users_and_units.json', 'courses_and_units.json']

	# Check the response if there is a data within

	def test_get(self):
		# self.client attribute will be an APIClient instance
		# Basically it will act as a client
		response = self.client.get(url_1)
		data = json.loads(response.content)["data"] # backend responses the API
		d_0 = data[0]
		self.assertIn("name", d_0) # Check if there is a "name" key on the API
		self.assertIn("description", d_0) # Check if there is a "description" key on the API
		self.assertIn("percentage", d_0) # Check if there is a "percentage" key on the API
		self.assertEqual(response.status_code, status.HTTP_200_OK) # Checks if the API has the right status of 200 OK

	@skip("Functionality not yet implemented")
	def test_post(self):
		x = _cls._setup_add_record(self)
		self.assertEqual(x[0].status_code, status.HTTP_201_CREATED) # Checks if the API has the right status of 201 CREATED
