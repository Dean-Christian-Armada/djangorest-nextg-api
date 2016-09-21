# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.accounts.models import UserAccount, UsersAndCourses
from core.models import Course, School, SchoolsAndCourses


class Command(BaseCommand):
	title = "Users and Courses"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+" Models"
		self.clear()
		print "Creating "+self.title+" Model"
		self.make_data()
		print "done"
	def make_data(self):
		school = School.objects.latest('id')
		x = UserAccount.objects.latest('id')
		course = Course.objects.create(name="Certificate III In Early ChildHood Education")
		z = SchoolsAndCourses.objects.create(school=school, course=course)
		UsersAndCourses.objects.create(user_account=x, school_course=z)

	def clear(self):
		Course.objects.all().delete()