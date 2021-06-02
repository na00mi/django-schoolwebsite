from django.contrib import admin
from schedule.models import Subject, Assignment
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subnum', 'subname')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=('assignnum', 'assigntitle')
