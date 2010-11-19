from django.db import models
from django.utils.translation import ugettext_lazy as _

from publisher.models import PublishableModel
from careers.constants import *


class JobPosition(PublishableModel):
    """
    A job position
    """
    title = models.CharField(_("Title"), max_length=255)
    prerequisites = models.TextField(_("Prerequisites"), blank=True)
    description = models.TextField(_("Description"), blank=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Job Position")
        verbose_name_plural = _("Job Positions")
        ordering = ["order", "-creation_date"]

    def __unicode__(self):
        return self.title


class JobApplication(models.Model):
    """
    A job application, tied to a JobPosition
    """
    position = models.ForeignKey(JobPosition, verbose_name=_("Position"), related_name="applications")
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    address = models.CharField(_("Address"), max_length=255)
    phone_number = models.CharField(_("Phone Number"), max_length=255)
    email = models.EmailField(_("Email"))
    comments = models.TextField(_("Comments"), blank=True)
    contact_time = models.PositiveSmallIntegerField(_("Best Time To Talk"), choices=APPLICATION_CONTACT_TIME_CHOICES, default=APPLICATION_CONTACT_TIME_MORNING)
    application_date = models.DateTimeField(_("Application Date"), auto_now_add=True)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _("Job Application")
        verbose_name_plural = _("Job Applications")
        ordering = ["application_date"]

    def __unicode__(self):
        return self.full_name
