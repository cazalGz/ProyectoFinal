from django.conf.urls.defaults import *
from mysite.views import current_datetime


urlpatterns = patterns('',
   (r'^time/$', current_datetime),
)