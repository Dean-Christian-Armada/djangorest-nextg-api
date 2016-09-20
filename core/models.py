from __future__ import unicode_literals

from django.db import models

from core.methods import school_logo_upload_path_handler

# Create your models here.

# Model used to know the available features to be used in the front-end mobile  
class FeatureToggle(models.Model):
	name = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

class School(models.Model):
	logo = models.ImageField(upload_to=school_logo_upload_path_handler)
	name = models.CharField(max_length=75)
	code = models.CharField(max_length=15)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
