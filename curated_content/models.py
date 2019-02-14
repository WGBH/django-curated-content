from django.db import models
from django.utils.translation import ugettext_lazy as _
from gatekeeper.models import GatekeeperSerialAbstractModel
from gatekeeper.utils import get_appropriate_object_from_model

class CuratedContentBlock(models.Model):
  """
  This is the curated object.  Only one of each of the instances
  of this object will be live at any given time.
  """
  title = models.CharField (
    _('Title'),
    max_length = 200,
    null = False
  )
  slug = models.SlugField (
    _('Slug'),
    unique = True,
    null = False
  )

  def __most_appropriate_item(self):
    items = self.curatedcontentinstance_set.all()
    print ("GOT HERE 0: ITEMS = ", items)
    item = get_appropriate_object_from_model(items, is_queryset=True)
    if item:
      return "%d: %s" % (item.pk, item.instance_title)
    else:
      return "(None)"
  most_appropriate_item = property(__most_appropriate_item)

  def __str__(self):
    return self.title

class CuratedContentInstance(GatekeeperSerialAbstractModel):
  """
  This is the model instance.
  """
  instance_title = models.CharField(
    _('Instance Title'),
    max_length = 200,
    null = False,
    help_text = 'Use this to describe what is different about this instance from the others, e.g., \"when service is offline\"'
  )
  content_block = models.ForeignKey(
    CuratedContentBlock,
    on_delete = models.CASCADE,
  )
  content = models.TextField(
    _('Content'),
    null = True, blank = True
  )
  
  def __str__(self):
    return "%s: %s" % (self.content_block.title, self.instance_title)
