from django.conf.urls import patterns, url

urlpatterns = patterns('auth.views',
    # Examples:
    # url(r'^$', 'Chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'logins', name='login'),
    url(r'^register/$', 'register', name='register'),
    url(r'^out/$', 'logout_view', name='out'),
)