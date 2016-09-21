from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from collections import OrderedDict

from core.models import School, AUState, SchoolsAndCourses, CoursesAndUnits

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
		return "%s %s %s" % (self.user.first_name, self.middle_name, self.user.last_name)

	def __unicode__(self):
		return self.get_name()

	def get_school(self):
		return {"name": self.school.name, "address": self.school.get_school_address()}

class UsersAndCourses(models.Model):
	user_account = models.ForeignKey(UserAccount)
	school_course = models.ForeignKey(SchoolsAndCourses)
	start = models.DateField(auto_now_add=True)
	end = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return "%s - %s" % (self.user_account, self.school_course)

class UsersAndUnits(models.Model):
	user_account = models.ForeignKey(UserAccount)
	course_unit = models.ForeignKey(CoursesAndUnits)

	def __unicode__(self):
		return "%s - %s" % (self.user_account, self.course_unit)

	# Temporary value
	def get_homework_percentage(self):
		return 15