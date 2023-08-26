from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myauth/', include('app_auth.urls')),
    path('', include('app.urls')),
    path('lesson_4', include('app_lesson_4.urls')),
    path('lesson_5', include('lesson_5.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
