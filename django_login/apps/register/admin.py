from django.contrib import admin

from .models import UserManager,User,UserInfo


admin.site.register(User)
admin.site.register(UserInfo)