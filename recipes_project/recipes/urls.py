from django.conf.urls import patterns, include, url
from recipes.views import food_list


urlpatterns = patterns('',
    url(r'^food/$', food_list, name='food-list')
        )