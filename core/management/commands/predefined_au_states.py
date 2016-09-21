# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.models import AUState

class Command(BaseCommand):
	title = "AU States"
	help = "My command for filling up the "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+"s"
		self.clear()
		print "Creating "+self.title+"s"
		self.make_data()
		print "done"
	def make_data(self):
		AUState.objects.create(name="New South Wales", code="NSW")
		AUState.objects.create(name="Queensland", code="QLD")
		AUState.objects.create(name="Tasmania", code="TAS")
		AUState.objects.create(name="Western Australia", code="WA")
		AUState.objects.create(name="South Australia", code="SA")
		AUState.objects.create(name="Victoria", code="VIC")

	def clear(self):
		AUState.objects.all().delete()