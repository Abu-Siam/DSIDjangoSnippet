from django.contrib import admin

from basicAuth.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','roll','city')
# Register your models here.
admin.site.register(Student,StudentAdmin)
