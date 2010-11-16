from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from events.models import EventCategory, Event


class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    search_fields = ("title",)

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": ("title", "order")
        }),
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "creation_date", "modification_date", "publication_date", "expiration_date", "published")
    search_fields = ("title", "content", "dates")
    date_hierarchy = "creation_date"
    list_filter = ("published", )

    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            "fields": ("title", "category", "url", "dates", "content", "order")
        }),
        (_("Publication Settings"), {
            "fields": ("publication_date", "expiration_date", "published")
        }),
    )


admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
