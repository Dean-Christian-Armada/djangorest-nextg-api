from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model used to know the available features to be used in the front-end mobile  
class FeatureToggle(models.Model):
	name = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name