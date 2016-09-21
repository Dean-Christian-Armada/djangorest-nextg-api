from django.contrib import admin

from . models import FeatureToggle, School, AUState, Unit

class FeatureToggleAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')

# Register your models here.
admin.site.register(FeatureToggle, FeatureToggleAdmin)
admin.site.register(School)
admin.site.register(AUState)
admin.site.register(Unit)