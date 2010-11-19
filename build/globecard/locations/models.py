from django.db import models
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField

from publisher.models import PublishableModel


class Location(PublishableModel):
    """
    A basic location with a title, contains Clients
    """
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    content = MarkupField(_("Content"), blank=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    @models.permalink
    def get_absolute_url(self):
        return ("locations_detail", (), {
            "slug": self.slug,
        })

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")
        ordering = ["order"]

    def __unicode__(self):
        return self.name


class Client(PublishableModel):
    """
    A Client, tied to a Location
    """
    location = models.ForeignKey(Location, verbose_name=_("Location"), related_name="clients")
    name = models.CharField(_("Name"), max_length=255)
    content = MarkupField(_("Content"), blank=True)
    image = models.ImageField(_("Image"), upload_to="files/clients", blank=True, null=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        ordering = ["order"]

    def __unicode__(self):
        return self.name
