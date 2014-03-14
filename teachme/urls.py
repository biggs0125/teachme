from django.conf.urls import patterns, include, url
from django.contrib import admin
import page.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teachme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', page.views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', page.views.homePage),
    url(r'^submission/',page.views.submission),
    url(r'^acceptSubmission/',page.views.acceptSubmission),
    url(r'^signup/',page.views.signup),
    url(r'^acceptSignup/',page.views.acceptSignup),
    url(r'^login/',page.views.login),
    url(r'^acceptLogin/',page.views.acceptLogin),
    url(r'^teachme/',page.views.instruction),
    url(r'^lessons/',page.views.lessons),
    url(r'^logout/',page.views.logout),
    url(r'^(.*)',page.views.userpage),
)
