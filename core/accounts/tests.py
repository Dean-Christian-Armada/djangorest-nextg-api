from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.tests import SetUserAccount

from rest_framework import status
from rest_framework.test import APITestCase

import json

# Create your tests here.

class LoginTest(APITestCase):
	url_login = reverse('login')

	fixtures = SetUserAccount.fixtures
	fixtures += ['users.json', 'applications.json', 'access_tokens.json']

	def test_login_failed(self):
		post_data = {"username": "deantest", "password": "armada13test"} # Client enter username and password

		response 		 = self.client.post(self.url_login, post_data) # Client makes a post request
		response_content = json.loads(response.content) # Content of API response

		self.assertEqual(0, len(response_content["data"])) # Check if data key in the content is empty
		self.assertNotEqual(0, len(response_content["errors"])) # Check if errors key in the content is not empty
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) # Check if the API response status is 400 Bad Request


	def test_login_success(self):
		post_data = {"username": "dean", "password": "armada13"} # Client enter username and password

		response 		 = self.client.post(self.url_login, post_data) # Client makes a post request
		response_content = json.loads(response.content) # Content of API response

		self.assertNotEqual(0, len(response_content["data"])) # Check if data key in the content is not empty
		self.assertIn("id", response_content["data"]) # Check value of data key if have an id key
		self.assertIn("school", response_content["data"]) # Check value of data key if have a school key
		self.assertIn("name", response_content["data"]["school"]) # Check value of school key in data if have a name key
		self.assertIn("address", response_content["data"]["school"]) # Check value of school key in data if have a address key
		self.assertIn("token", response_content["data"]) # Check value of data key if have a token key
		self.assertEqual(0, len(response_content["errors"])) # Check if errors key in the content is empty
		self.assertEqual(response.status_code, status.HTTP_200_OK) # Check if the API response status is 200 OK

	def test_login_too_many_requests(self):
		post_data = {"username": "deantest", "password": "armada13test"} # Client enter username and password

		response 		 = self.client.post(self.url_login, post_data) # Client makes a post request
		response_content = json.loads(response.content) # Content of API response

		for n in range(0, 4):

