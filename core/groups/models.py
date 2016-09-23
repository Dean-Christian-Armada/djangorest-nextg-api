from __future__ import unicode_literals

from django.db import models

from core.accounts.models import UserAccount
from core.methods import group_picture_upload_path_handler

# Create your models here.
class Group(models.Model):
	created_by = models.ForeignKey(UserAccount)
	name = models.CharField(max_length=100)
	description = models.TextField()
	picture = models.ImageField(upload_to=group_picture_upload_path_handler, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class UsersAndGroups(models.Model):
	user_account = models.ForeignKey(UserAccount)
	group = models.ForeignKey(Group)
	date_joined = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s" % (self.group.name, self.user_account.get_name())