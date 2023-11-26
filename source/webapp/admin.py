from django.contrib import admin
from webapp.models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'date_of_completion']
    readonly_fields = ['date_of_completion']

admin.site.register(Task, TaskAdmin)
