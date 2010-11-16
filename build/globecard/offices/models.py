from django.db import models
from django.utils.translation import ugettext_lazy as _

from publisher.models import PublishableModel


class Office(PublishableModel):
    """
    An office, with address and contact information
    """
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    image = models.ImageField(_("Image"), upload_to="files/offices", blank=True, null=True)
    address = models.CharField(_("Address"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    province = models.CharField(_("Province"), max_length=255, blank=True)
    country = models.CharField(_("Country"), max_length=255, blank=True)
    postal_code = models.CharField(_("Postal Code"), max_length=255, blank=True)
    fax_number = models.CharField(_("Fax Number"), max_length=255, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=255, blank=True)
    email = models.EmailField(_("Email"), blank=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    @models.permalink
    def get_absolute_url(self):
        return ("offices_detail", (), {
            "slug": self.slug,
        })

    class Meta:
        verbose_name = _("Office")
        verbose_name_plural = _("Offices")
        ordering = ["order"]

    def __unicode__(self):
        return self.name
