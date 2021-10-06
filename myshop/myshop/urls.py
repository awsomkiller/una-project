from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views #ADD THIS LINE

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name="welcome page" ),
    path('products/', include('products.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
