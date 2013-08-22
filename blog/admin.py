from django.contrib import admin
from blog.models import Post
from resume.models import Education, Employer, Job, Responsibility, Accomplishment, Tech, HardSkill, SoftSkill

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Education)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Responsibility)
admin.site.register(Accomplishment)
admin.site.register(Tech)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)