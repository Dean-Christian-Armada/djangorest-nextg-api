# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.models import AUState

class Command(BaseCommand):
	help = "My command for filling up the AU States Model"
	def handle(self, *args, **options):
		print "Deleting Current AU States"
		self.clear()
		print "Creating AU States"
		self.make_au_states()
		print "done"
	def make_au_states(self):
		AUState.objects.create(name="New South Wales", code="NSW")
		AUState.objects.create(name="Queensland", code="QLD")
		AUState.objects.create(name="Tasmania", code="TAS")
		AUState.objects.create(name="Western Australia", code="WA")
		AUState.objects.create(name="South Australia", code="SA")
		AUState.objects.create(name="Victoria", code="VIC")

	def clear(self):
		AUState.objects.all().delete()