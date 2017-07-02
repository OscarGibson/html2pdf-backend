from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','user','date')
    class Meta:
        model = Project
admin.site.register(Project, ProjectAdmin)
