from rest_framework import serializers

from collections import OrderedDict

from core.models import FeatureToggle

class FeatureTogglingSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeatureToggle
		fields = ('name', 'status')

	def to_representation(self, instance):
		ret = super(FeatureTogglingSerializer, self).to_representation(instance)
		# START removes null album
		x = ret.items()
		index = self.Meta.fields.index('status')
		if not x[index]:
			del x[index]
		ret = OrderedDict(list(filter(lambda x: x[1], x)))
		# END removes null album
		# ret = OrderedDict(list(filter(lambda x: x[1], ret.items()))) # removes every null field
		return ret