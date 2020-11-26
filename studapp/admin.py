from django.contrib import admin
from studapp.models import stud

# Register your models here.
class StudAdmin(admin.ModelAdmin):
	pass
admin.site.register(stud,StudAdmin)
