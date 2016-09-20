from rest_framework import serializers

from collections import OrderedDict

from core.models import FeatureToggle

class FeatureTogglingSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeatureToggle
		fields = ('name', 'status')