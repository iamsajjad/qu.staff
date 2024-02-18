
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#Handling Language
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(

    # Django Admin Page
    path('admin/', admin.site.urls),

    # User URLs
    path('user/', include('user.urls')),

    # History URLs
    path('history/', include('history.urls')),

    # Settings URLs
    path('settings/', include('settings.urls')),

    # Search URLs
    path('search/', include('search.urls')),

    # Home URLs
    path('', include('home.urls')),
    path('home/', include('home.urls')),

    # Bio URLs
    path('@/', include('bio.urls')),

    # Link URLs
    path('bio/link/', include('link.urls')),

    # Publication URLs
    path('bio/publication/', include('publication.urls')),

    # debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

    # Language Prefix
    prefix_default_language=True,
)

# Handling Errors
handler404 = 'error.views.error404'
handler500 = 'error.views.error500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

