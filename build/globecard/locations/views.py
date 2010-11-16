from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from locations.models import Location


def landing(request):
    """
    Redirects to the first available Location
    """
    try:
        location = Location.objects.all()[0]
    except IndexError:
        raise Http404

    return HttpResponseRedirect(location.get_absolute_url())


def detail(request, slug):
    """
    Renders Location with the given slug
    """
    location = get_object_or_404(Location, slug=slug)
    locations = Location.objects.all()

    return render_to_response("locations/detail.html", {
        "location": location,
        "locations": locations,
    }, context_instance=RequestContext(request))
