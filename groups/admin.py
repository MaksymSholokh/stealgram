from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass