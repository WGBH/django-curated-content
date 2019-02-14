from django import template
from gatekeeper.utils import get_appropriate_object_from_model
from ..models import CuratedContentBlock

register = template.Library()

@register.simple_tag
def curated_content(slug):
  try:
    block = CuratedContentBlock.objects.get(slug=slug)
  except:
    return None

  items = block.curatedcontentinstance_set.all()
  item = get_appropriate_object_from_model(items, is_queryset=True)
  return item