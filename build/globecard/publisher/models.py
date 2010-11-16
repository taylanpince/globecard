from django.db import models

from publisher.managers import PublishableModelManager


class PublishableModel(models.Model):
    """
    A base model that has the usual publication options, along with a default manager
    """
    creation_date = models.DateTimeField(_("Created"), auto_now_add=True)
    modification_date = models.DateTimeField(_("Modified"), auto_now=True)
    publication_date = models.DateTimeField(_("Publication Date"), blank=True, null=True)
    expiration_date = models.DateTimeField(_("Expiration Date"), blank=True, null=True)
    published = models.BooleanField(_("Published"), default=True)

    admin_objects = models.Manager()
    objects = PublishableModelManager()

    class Meta:
        abstract = True
        verbose_name = _("Publishable Model")
        verbose_name_plural = _("Publishable Models")

    def __unicode__(self):
        return u"Publishable Model"
