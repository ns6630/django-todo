from django.contrib import admin

from core.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Todo, TodoAdmin)
