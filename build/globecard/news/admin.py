from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from news.models import NewsEntry


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_date", "modification_date", "publication_date", "expiration_date", "published")
    search_fields = ("title", "content")
    list_filter = ("published", )
    prepopulated_fields = {
        "slug": ("title",),
    }

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "image", "content")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


admin.site.register(NewsEntry, NewsEntryAdmin)
