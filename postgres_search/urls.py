from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from search.views import StudentSearchListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'postgres_search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^index/', TemplateView.as_view(template_name = 'index.html')),
    url('^search/', StudentSearchListView.as_view())
)
