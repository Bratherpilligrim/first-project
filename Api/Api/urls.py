from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from main.router import router
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/home' ,HomeViews ,),
    path('api/about' ,AboutView ,)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
