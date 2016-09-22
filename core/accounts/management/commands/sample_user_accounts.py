# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from oauth2_provider.models import Application

from core.accounts.models import UserAccount, UserType
from core.models import School, AUState
from core.vars import token_url

from requests.auth import HTTPBasicAuth
import requests

import json

class Command(BaseCommand):
	title = "User Account"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		# print "Deleting Current "+self.title+"s"
		# self.clear()
		print "Creating "+self.title+"s"
		self.make_data()
		print "done"
	def make_data(self):
		state = AUState.objects.get(code="QLD")
		street = "General Kalentong Street"
		suburb = "Mandaluyong"
		post_code = 1200
		try:
			user = User.objects.get(first_name="Dean", last_name="Armada", username="dean")
			user = UserAccount.objects.get(id=8)
			print "/////"
			print "Already Existing"
		except:
			print "Creating New Users"
			self.clear()
			user_type = UserType.objects.get(name="Student")
			user = User.objects.create_user(id=2, username="dean", password="armada13", email="deanarmada@looplabs.com.au", first_name="Dean", last_name="Armada")
			app = Application.objects.create(name="Sample ORM", client_type="public", authorization_grant_type="password", user=user)
			data = "grant_type=password&username=dean&password=armada13"
			headers = {"content-type": "application/x-www-form-urlencoded"}
			r = requests.post(token_url, data=data, auth=(app.client_id, app.client_secret), headers=headers)
			print "ACCESS TOKEN  "+json.loads(r.content)['access_token']
			school = School.objects.create(name="Don Bosco Technical College", code="DBTC", street=street, suburb=suburb, state=state, post_code=post_code)
			UserAccount.objects.create(id=8, user=user, user_type=user_type, school=school, middle_name="Guinto", street=street, suburb=suburb, state=state, post_code=post_code)

	def clear(self):
		UserAccount.objects.all().delete()
		School.objects.all().delete()
		User.objects.filter(is_superuser=False).delete()
		Application.objects.all().delete()