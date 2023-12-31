
from django.contrib import admin
from django.urls import path
from youtube import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('upload',views.upload,name='upload'),
    path('video/<int:pk>',views.video_detail,name='video_detail'),
    path('comment',views.comment,name='comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)