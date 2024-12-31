from django.contrib import admin
from notice.models import Platform, Status

class PlatformAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

class StatusAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Status, StatusAdmin)