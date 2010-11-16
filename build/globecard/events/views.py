from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from events.models import EventCategory, Event


def list(request):
    """
    Renders all EventCategory objects that have available Events
    """
    categories = EventCategory.objects.filter(events_isnull=False)

    return render_to_response("events/list.html", {
        "categories": categories,
    }, context_instance=RequestContext(request))
