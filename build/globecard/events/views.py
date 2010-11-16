from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from events.models import Event


def list(request):
    """
    Renders all EventCategory objects that have available Events
    """
    events = Event.objects.all()

    return render_to_response("events/list.html", {
        "events": events,
    }, context_instance=RequestContext(request))
