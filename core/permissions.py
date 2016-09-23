from rest_framework import status, permissions

from core.accounts.models import UserAccount

# TODO: Use ElasticSearch
class StudentPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		try:
			x = UserAccount.objects.get(user=request.user).user_type.name
			if x.lower() == "student":
				return 1
			else:
				return 0
		except:
			return 0