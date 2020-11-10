from django.contrib import admin

from university.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display_links = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'grade']


admin.site.register(Student, StudentAdmin)
