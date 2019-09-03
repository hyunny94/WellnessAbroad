from django.contrib import admin
from event.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time', 'location']


admin.site.register(Event, EventAdmin)
