from rest_framework import serializers

from core.accounts.models import UsersAndUnits

class UnitsAndUsersSerializer(serializers.ModelSerializer):
	name = serializers.CharField(source="course_unit.unit.name", read_only=True)
	description = serializers.CharField(source="course_unit.unit.description", read_only=True)
	percentage = serializers.IntegerField(source="get_homework_percentage", read_only=True)
	class Meta:
		model = UsersAndUnits
		fields = ('name', 'description', 'percentage')