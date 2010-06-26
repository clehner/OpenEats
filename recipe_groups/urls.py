from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update
from models import Course, Cuisine

course_info={
                "queryset":Course.objects.all(),
                "template_object_name":"course",
            }
cuisine_info={
                "queryset":Cuisine.objects.all(),
                "template_object_name": "cuisine",
             }
urlpatterns = patterns('',
    (r'^add/course/$', 'openeats.recipe_groups.views.course_pop'),
    (r'^course/$', list_detail.object_list, course_info ),
    (r'^course/new/$', create_update.create_object, dict({'model':Course,}, login_required=True, post_save_redirect='/recipe/')),
    url(r'^course/(?P<slug>[-\w]+)/$', 'openeats.recipe_groups.views.course_recipes', name="course_recipes"),
    (r'^cuisine/$', list_detail.object_list, cuisine_info),
    (r'^cuisine/new/$', create_update.create_object, dict({'model':Cuisine,}, login_required=True, template_name='recipe_groups/course_form.html', post_save_redirect='/recipe/')),
    url(r'^cuisine/(?P<slug>[-\w]+)/$', 'openeats.recipe_groups.views.cuisine_recipes', name="cuisine_recipes"),

)