from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('default/admin/', admin.site.urls),
    path('admin/', include("admin_panel.urls")), # Our Custom Admin Panel URLs
    path('', include("public_panel.urls")), # 
    path('tinymce/', include('tinymce.urls')),
]


# from django.conf import settings
from core import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
