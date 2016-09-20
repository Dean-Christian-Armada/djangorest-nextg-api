from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class LoginTest(APITestCase):
	url_login = reverse('login')

	def test_get(self):
		response = self.client.get(self.url_login)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content, 'dean')

