from django.contrib import admin
from django.urls import path
from notice.views import index
from django.conf import settings
from django.conf.urls.static import static
from notice.views import NewPlatformCreateView, NewStatusCreateView, PlatformListView, PlatformUpdateView, PlatformDeleteView, StatusListView,StatusDeteleView, StatusUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('new_platform/', NewPlatformCreateView.as_view(), name='new_platform'),
    path('new_status/', NewStatusCreateView.as_view(), name='new_status'),
    path('platform/', PlatformListView.as_view(), name='platforms' ),
    path('platform/<int:pk>/update', PlatformUpdateView.as_view(), name='platform_update'),
    path('platform/<int:pk>/delete', PlatformDeleteView.as_view(), name='platform_delete'),
    path('status/', StatusListView.as_view(), name='status' ),
    path('status/<int:pk>/update', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete', StatusDeteleView.as_view(), name='status_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

