from django.contrib import admin

# Register your models here.
from django.contrib import admin
from authentication.models import SparkUser

# Register your models here.


class SparkUserAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(SparkUser, SparkUserAdmin)
