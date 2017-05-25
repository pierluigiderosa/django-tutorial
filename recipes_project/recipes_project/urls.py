from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipes_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^recipes_project/', include('recipes_project.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipes/', include('recipes.urls')),
)
