from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Intern)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Staff)
admin.site.register(NonStaff)
admin.site.register(Report)
admin.site.register(LabTest)
admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Message)
admin.site.register(NewsUpdate)
admin.site.register(TBPatient)
@admin.register(DiseaseTest)
class DiseaseTestAdmin(admin.ModelAdmin):
    list_display = ('disease_name', 'test_count')
    search_fields = ('disease_name',)
    list_filter = ('disease_name',)
    ordering = ('-test_count',)
