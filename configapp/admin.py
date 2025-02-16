from django.contrib import admin
from .models import Kurs, Student


class KursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_time', 'end_time')
    list_display_links = ('id', 'title')
    search_fields = ['title']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email', 'kurs')
    list_display_links = ('id', 'full_name')
    search_fields = ['full_name','id']

admin.site.register(Student,StudentAdmin)
admin.site.register(Kurs,KursAdmin)

