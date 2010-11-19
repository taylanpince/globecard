from django.db import models
from django.utils.translation import ugettext_lazy as _

from publisher.models import PublishableModel


class NewsEntry(PublishableModel):
    """
    A news item
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    image = models.ImageField(_("Image"), upload_to="files/news", blank=True, null=True)
    content = models.TextField(_("Content"), blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ("news_detail", (), {
            "slug": self.slug,
        })

    class Meta:
        verbose_name = _("News Entry")
        verbose_name_plural = _("News Entries")
        ordering = ["-creation_date"]

    def __unicode__(self):
        return self.title
