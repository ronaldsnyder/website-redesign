from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage_redesign1.views.home', name='home'),
    # url(r'^homepage_redesign1/', include('homepage_redesign1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'resume.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)
