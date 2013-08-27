from django.contrib import admin
from resume.models import Education, Employer, Job, Responsibility, Accomplishment, Tech, HardSkill, SoftSkill
   
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'college', 'start', 'end']
    

admin.site.register(Education, EducationAdmin)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Responsibility)
admin.site.register(Accomplishment)
admin.site.register(Tech)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)