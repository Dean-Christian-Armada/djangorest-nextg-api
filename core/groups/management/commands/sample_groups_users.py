# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.accounts.models import UserAccount
from core.groups.models import Group, UsersAndGroups


class Command(BaseCommand):
	title = "Groups and Users"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+" Models"
		self.clear()
		print "Creating "+self.title+" Model"
		self.make_data()
		print "done"
	def make_data(self):
		groups = Group.objects.filter()
		users = UserAccount.objects.filter()
		for x in groups:
			for _user in users:
				UsersAndGroups.objects.create(user_account=_user, group=x)

	def clear(self):
		UsersAndGroups.objects.all().delete()