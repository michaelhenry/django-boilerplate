from django.urls import (path, include)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', admin.site.urls),
  path('v1/token/', obtain_auth_token, name='auth-token'),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# STATIC FILES
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PAGES
urlpatterns += [

 ]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns  += [
      path('__debug__/', include(debug_toolbar.urls)),
  ]


admin.site.site_header      =    'Django-Boilerplate'
admin.site.site_title       =    'Django-Boilerplate'
admin.site.site_url         =     None