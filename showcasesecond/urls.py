
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('myapp.urls')),
  path('paypal/', include('paypal.standard.ipn.urls')),
]
urlpatterns = urlpatterns +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)