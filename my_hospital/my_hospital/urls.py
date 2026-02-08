from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Desktop admin root: show our custom admin login when people visit '/admin/'
    path('admin/', RedirectView.as_view(url='/admin/login/', permanent=False)),
    # Keep Django admin available at a different path in case you need it
    path('superadmin/', admin.site.urls),
    path('', include('members.urls')),
]

# Serve static files during development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()