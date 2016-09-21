# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.models import Unit

class Command(BaseCommand):
	title = "Unit"
	help = "My command for filling up samples of "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+"s"
		self.clear()
		print "Creating "+self.title+"s"
		self.make_data()
		print "done"
	def make_data(self):
		Unit.objects.create(name="CHCLEG001", description="Work legally and ethically")
		Unit.objects.create(name="CHCCE009", description="Used an approved learning framework to guide practice")

	def clear(self):
		Unit.objects.all().delete()