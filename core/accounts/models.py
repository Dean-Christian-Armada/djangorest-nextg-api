from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.models import School, AUState

# Create your models here.

class UserType(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class UserAccount(models.Model):
	user = models.ForeignKey(User)
	user_type = models.ForeignKey(UserType)
	school = models.ForeignKey(School)
	middle_name = models.CharField(max_length=50)
	street = models.TextField()
	suburb = models.CharField(max_length=75)
	state = models.ForeignKey(AUState)
	post_code = models.IntegerField()
	last_login = models.DateTimeField(auto_now_add=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def get_name(self):
		return "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)

	def __unicode__(self):
		return self.get_name()