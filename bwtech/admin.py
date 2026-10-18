from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Contact)

admin.site.register(Service)

admin.site.register(Booking)

admin.site.register(Country)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    search_fields = ('name', 'location')