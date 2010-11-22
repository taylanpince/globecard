from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "creation_date", "modification_date", "publication_date", "expiration_date", "published", "order", "landing")
    search_fields = ("title", "content")
    list_filter = ("published", "section", "landing")
    prepopulated_fields = {
        "slug": ("title",),
    }

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "section", "content", "image", "order", "landing")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


admin.site.register(Page, PageAdmin)
