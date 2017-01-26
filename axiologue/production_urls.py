from django.conf.urls import include, url
from django.contrib import admin

from .views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view()),
    url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
