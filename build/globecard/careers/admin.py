from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from careers.models import JobPosition, JobApplication


class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_date", "modification_date", "publication_date", "expiration_date", "published", "order")
    search_fields = ("title", "prerequisites", "description")
    list_filter = ("published", )

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": ("title", "prerequisites", "description", "order")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "email", "phone_number", "application_date")
    search_fields = ("first_name", "last_name", "comments", "email", "address", "phone_number")

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": (("first_name", "last_name"), "position", "comments")
        }),
        (_("Contact Details"), {
            "fields": ("address", "phone_number", "email", "contact_time")
        }),
    )


admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
