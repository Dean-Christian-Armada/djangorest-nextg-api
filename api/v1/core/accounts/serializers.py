from django.contrib.auth.models import User

from rest_framework import serializers

from collections import OrderedDict

from core.accounts.models import UserAccount


class LoginAuthenticationSerializer(serializers.ModelSerializer):
	school = serializers.DictField(source="get_school", read_only=True)
	class Meta:
		model 	= UserAccount
		fields 	= ('id', 'school')