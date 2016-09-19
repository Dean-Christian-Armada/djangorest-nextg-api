from django.contrib import admin

from . models import FeatureToggle

class FeatureToggleAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')

# Register your models here.
admin.site.register(FeatureToggle, FeatureToggleAdmin)