from django.contrib import admin
from studapp.models import stud
from studapp.models import course

# Register your models here.
class StudAdmin(admin.ModelAdmin):
	pass
admin.site.register(stud,StudAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(course,CourseAdmin)
