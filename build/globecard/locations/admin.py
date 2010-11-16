from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from locations.models import Location, Client


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "creation_date", "modification_date", "publication_date", "expiration_date", "published", "order")
    search_fields = ("name", "content")
    list_filter = ("published", )
    prepopulated_fields = {
        "slug": ("name",),
    }

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": (("name", "slug"), "content", "order")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "creation_date", "modification_date", "publication_date", "expiration_date", "published", "order")
    search_fields = ("name", "content")
    list_filter = ("published", )

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": ("name", "location", "content", "order")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


admin.site.register(Location, LocationAdmin)
admin.site.register(Client, ClientAdmin)
