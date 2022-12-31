from django.contrib import admin

from .models import Report, TypeOfRoad, Location, AccidentType


admin.site.register([TypeOfRoad, Location, AccidentType])

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['witness_name', 'date_of_accident', 'time_of_accident', 'is_fatal', 'accident_type', 'status', 'location']
    list_filter = ['is_fatal', 'accident_type', 'status', 'location', 'date_of_accident']
    search_fields = ['witness_name']
    date_hierarchy = 'date_of_accident'
