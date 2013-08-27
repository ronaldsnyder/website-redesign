from django.conf.urls import patterns, include, url

from resume import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage_redesign1.views.home', name='home'),
    # url(r'^homepage_redesign1/', include('homepage_redesign1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'resume.views.index', name='resume-index'),
    url(r'^experience$', 'resume.views.experience', name='experience'),
    url(r'^skills$', 'resume.views.skills', name='skills'),
    url(r'^education$', 'resume.views.education', name='education'),
)
