from django.db import models
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField

from pages.constants import *
from publisher.models import PublishableModel


class Page(PublishableModel):
    """
    A page, tied to a section
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    content = MarkupField(_("Content"), blank=True)
    image = models.ImageField(_("Image"), upload_to="files/pages", blank=True, null=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)
    section = models.CharField(_("Section"), choices=SECTION_CHOICES, default=SECTION_HOME, max_length=255)

    @models.permalink
    def get_absolute_url(self):
        return ("pages_detail", (), {
            "section": self.section,
            "slug": self.slug,
        })

    @property
    def base_template(self):
        return "%s/base.html" % self.section

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        ordering = ["section", "order"]

    def __unicode__(self):
        return u"%s > %s" % (self.get_section_display(), self.title)
