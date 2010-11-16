from django.db import models
from django.utils.translation import ugettext_lazy as _

from publisher.models import PublishableModel


class EventCategory(models.Model):
    """
    An event category, contains events
    """
    title = models.CharField(_("Title"), max_length=255)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Event Category")
        verbose_name_plural = _("Event Categories")
        ordering = ["order"]

    def __unicode__(self):
        return self.title


class Event(PublishableModel):
    """
    An event, tied to an EventCategory
    """
    category = models.ForeignKey(EventCategory, verbose_name=_("Category"), related_name="events")
    title = models.CharField(_("Title"), max_length=255)
    url = models.URLField(_("Web Site"), blank=True, null=True, verify_exists=True)
    dates = models.CharField(_("Dates"), blank=True, max_length=255)
    content = models.TextField(_("Content"), blank=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["order"]

    def __unicode__(self):
        return self.title
