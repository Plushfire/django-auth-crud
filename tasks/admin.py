from django.contrib import admin
from tasks import models

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(models.Task, TaskAdmin)