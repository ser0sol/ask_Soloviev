from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_Soloviev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','main.views.index', name = 'baze'),
   
    url(r'^signup$','main.views.reg', name ='signup'),
    url(r'^ask/$','main.views.ask', name = 'ask'),
    url(r'^login$','main.views.signin', name = 'login'),
    url(r'^hot/(?P<page>\d+)?/?$','main.views.hot', name = 'hot'), 
    url(r'^new/(?P<page>\d+)?/?$','main.views.newest', name = 'newest'),  
    url(r'^tag/(?P<tagname>\w+)?/(?P<page>\d+)?/?$','main.views.tag', name = 'tag'),   
   # url(r'^search/$','main.views.search'),
  #  url(r'^getparametrs$','main.views.getparametrs'),
    url(r'^question/(?P<question_id>\d+)/(?P<page>\d+)?/?','main.views.question', name = 'question'),
    url(r'^(?P<page>\d+)?/?','main.views.index'),
)
