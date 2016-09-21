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

class AUState(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10)

	def __unicode__(self):
		return self.code

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

class Course(models.Model):
	name = models.CharField(max_length=75)
	code = models.CharField(max_length=15)

	def __unicode__(self):
		return self.name

class SchoolsAndCourses(models.Model):
	school = models.ForeignKey(School)
	course = models.ForeignKey(Course)

	def __unicode__(self):
		return "%s - %s" % (self.school.name, self.course.name)

class Unit(models.Model):
	name = models.CharField(max_length=10)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class CoursesAndUnits(models.Model):
	school_course = models.ForeignKey(SchoolsAndCourses)
	unit = models.ForeignKey(Unit)

	def __unicode__(self):
		return "%s - %s" % (self.school_course, self.unit)