from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.methods import school_logo_upload_path_handler

# Create your models here.

# Model used to know the available features to be used in the front-end mobile  
class FeatureToggle(models.Model):
	name = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

class AUState(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10)

class School(models.Model):
	logo = models.ImageField(upload_to=school_logo_upload_path_handler)
	name = models.CharField(max_length=75)
	code = models.CharField(max_length=15)
	street = models.TextField()
	suburb = models.CharField(max_length=75)
	state = models.ForeignKey(AUState)
	post_code = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class UserType(models.Model):
	name = models.CharField(max_length=50)

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