from rest_framework import serializers

from core.accounts.models import UsersAndUnits

class UnitsAndUsersSerializer(serializers.ModelSerializer):
	units = serializers.ListField(source="get_student_units",read_only=True)
	class Meta:
		model = UsersAndUnits
		fields = ('user_account', 'course_unit')