from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from offices.models import Office


class OfficeAdmin(admin.ModelAdmin):
    list_display = ("name", "creation_date", "modification_date", "publication_date", "expiration_date", "published", "order")
    search_fields = ("name", "address", "city", "province", "country", "postal_code")
    list_filter = ("published", )
    prepopulated_fields = {
        "slug": ("name",),
    }

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": (("name", "slug"), "image", "order")
        }),
        (_("Address"), {
            "fields": ("address", ("city", "province"), ("country", "postal_code"))
        }),
        (_("Contact Information"), {
            "fields": ("fax_number", "phone_number", "email")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


admin.site.register(Office, OfficeAdmin)
