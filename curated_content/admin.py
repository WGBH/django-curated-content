from django.contrib import admin 
from gatekeeper.admin import GatekeeperSerialAdmin
from gatekeeper.utils import get_appropriate_object_from_model
from .models import CuratedContentBlock, CuratedContentInstance

class CuratedContentBlockAdmin(admin.ModelAdmin):
  list_display = ['pk', 'title', 'most_appropriate_item']
  prepopulated_fields = {'slug': ('title',)}

class CuratedContentInstanceAdmin(GatekeeperSerialAdmin):
  model = CuratedContentInstance
  list_display = ['pk', 'instance_title', 'content_block',]
  list_display_links = ['pk', 'instance_title']
  list_filter = ['content_block']
  search_fields = ['instance_title', 'content_block__title']
    
  fieldsets = [
    (None, {
      'fields': ( 'instance_title', 'content_block','content'),
    }),
  ]

  def is_live(self, obj):
    """
    This OVERRIDES the is_live method in GatekeeperSerialAdmin.
    """
    items = CuratedContentInstance.objects.filter(content_block=obj.content_block)
    live_item = get_appropriate_object_from_model(items, is_queryset=True)
    if obj == live_item:
      return True
    return False

admin.site.register(CuratedContentBlock, CuratedContentBlockAdmin)
admin.site.register(CuratedContentInstance, CuratedContentInstanceAdmin)