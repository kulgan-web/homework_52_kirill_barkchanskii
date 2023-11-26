from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['description', 'date_of_completion']
    search_fields = ['description', 'status', 'date_of_completion']
    fields = ['description', 'status', 'date_of_completion']
    readonly_fields = ['date_of_completion']


