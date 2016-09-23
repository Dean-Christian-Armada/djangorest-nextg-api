# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.accounts.models import UserAccount
from core.groups.models import Group

class Command(BaseCommand):
	title = "Group"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+"s"
		self.clear()
		print "Creating "+self.title+"s"
		self.make_data()
		print "done"
	def make_data(self):
		user = UserAccount.objects.get(user__username="dean")
		Group.objects.create(created_by=user, name="Sample Group 1", description="Just Another Sample")
		Group.objects.create(created_by=user, name="Sample Group 2", description="Just Another Sample")

	def clear(self):
		Group.objects.all().delete()