from django.contrib import admin

# Register your models here.

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'technology', 'description']
    list_display = ('title', 'technology')


admin.site.register(Project, ProjectAdmin)
