from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    # Examples:
    # url(r'^$', 'Chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', name='index'),
)
