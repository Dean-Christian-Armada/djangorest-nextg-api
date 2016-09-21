from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from unittest import skip # This library is used to skip some class TestCase

from core.tests import OauthAccessToken
from store.models import Artist
 
import time # This library is used in case you want to put a sleep before proceeding to the next line of scripts
import inspect # This library is used to print the method of that certain class.. inspect.stack()[0][3]
import json # This library is for parsing the response.content

# Create your tests here.

url_1 = reverse('students-units-list') # The URL endpoint for the artists which is /artists/ having POST and GET methods

# Reusabality Class
class StudentRecordSetupMixing():
	# For reusable of adding a single record
	# To be used for POST, GET(detailed), PUT and DELETE
	def _setup_add_record(self):
		OauthAccessToken.setUp(self) # This is declared to insert the Oauth without interrupting anything from the children classes
		_data = {"name": "50 Cent", "birth_date":"2005-02-13"}
		response = self.client.post(url_1, _data)
		data = json.loads(response.content)["data"]
		return ( response, _data, data )

_cls = StudentRecordSetupMixing # Variable for the re-usable class

class StudentTestWithoutData(OauthAccessToken):
	fixtures = list(OauthAccessToken.fixtures) # "list" is needed so the addressing of fixtures is different
	def test_get(self):
		response = self.client.get(url_1)
		data = json.loads(response.content)["data"]
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Check the response if there is given data
class StudentTestWithData(OauthAccessToken):
	fixtures = list(OauthAccessToken.fixtures) # "list" is needed so the addressing of fixtures is different

	# Check the response if there is a data within

	def test_get(self):
		# self.client attribute will be an APIClient instance
		# Basically it will act as a client
		response = self.client.get(url_1)
		data = json.loads(response.content)["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		# self.assertNotEqual(len(data), 0) # There should be a data
		# print ("%s.%s DONE - 1" % (self.__class__.__name__, inspect.stack()[0][3]))

	# @skip("Functionality not yet implemented")
	def test_post(self):
		x = _cls._setup_add_record(self)
		self.assertEqual(x[0].status_code, status.HTTP_201_CREATED) # Status 201 is the default when a new object is created 
		# self.assertEqual(x[2], x[1]) # have the API return the updated (or created) representation as part of the response
		# self.assertEqual(Artist.objects.count(), 1) # Make  sure that there is a craeted instance
		# self.assertEqual(x[0]["Location"], Artist.objects.get().get_absolute_url())
