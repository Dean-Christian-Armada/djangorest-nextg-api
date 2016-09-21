# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.accounts.models import UserType

class Command(BaseCommand):
	help = "My command for filling up the AU States Model"
	def handle(self, *args, **options):
		print "Deleting Current User Types"
		self.clear()
		print "Creating User Types"
		self.make_data()
		print "done"
	def make_data(self):
		UserType.objects.create(name="Student")
		UserType.objects.create(name="Assessor")
		UserType.objects.create(name="Supervisor")

	def clear(self):
		UserType.objects.all().delete()