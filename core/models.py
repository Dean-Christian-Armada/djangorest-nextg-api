from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model used to know the available features used,  
class FeaturedToggling(models.Model):
	name = models.CharField(max_length=100)
	status = models.BooleanField(default=0)