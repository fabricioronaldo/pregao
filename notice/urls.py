from django.contrib import admin
from django.urls import path
from notice.views import index
from django.conf import settings
from django.conf.urls.static import static
from notice.views import NewPlatformCreateView, NewStatusCreateView, PlatformListView, PlatformUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('new_platform/', NewPlatformCreateView.as_view(), name='new_platform'),
    path('new_status/', NewStatusCreateView.as_view(), name='new_status'),
    path('platform/', PlatformListView.as_view(), name='platforms' ),
    path('platform/<int:pk>/update', PlatformUpdateView.as_view(), name='platform_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

