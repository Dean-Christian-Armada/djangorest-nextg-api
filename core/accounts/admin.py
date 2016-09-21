from django.contrib import admin

from . models import UserType, UserAccount, UsersAndCourses, UsersAndUnits

# Register your models here.
admin.site.register(UserType)
admin.site.register(UserAccount)
admin.site.register(UsersAndCourses)
admin.site.register(UsersAndUnits)