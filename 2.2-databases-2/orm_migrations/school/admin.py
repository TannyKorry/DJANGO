from django.contrib import admin

from .models import Student, Teachers


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['name', 'teacher', 'group']


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
