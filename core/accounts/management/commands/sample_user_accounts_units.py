# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.accounts.models import UserAccount, UsersAndUnits, CoursesAndUnits
from core.models import Unit, SchoolsAndCourses


class Command(BaseCommand):
	title = "Users and Units"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+" Models"
		self.clear()
		print "Creating "+self.title+" Model"
		self.make_data()
		print "done"
	def make_data(self):
		units = Unit.objects.filter()
		users = UserAccount.objects.filter()
		school_course = SchoolsAndCourses.objects.latest('id')
		for x in units:
			y = CoursesAndUnits.objects.create(school_course=school_course, unit_id=x.id)
			for _user in users:
				UsersAndUnits.objects.create(user_account=_user, course_unit=y)

	def clear(self):
		UsersAndUnits.objects.all().delete()