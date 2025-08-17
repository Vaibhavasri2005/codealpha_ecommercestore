from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import register  # ✅ only needed if you use register view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),  # ✅ ADD THIS LINE
    path('', include('store.urls')),  # ✅ include app urls
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Django built-in login/logout
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
