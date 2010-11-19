from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from pages.models import Page


def landing(request, section):
    """
    Tries to match a landing page for the given section
    """
    try:
        page = Page.objects.filter(section=section)[0]
    except IndexError:
        raise Http404

    return HttpResponseRedirect(page.get_absolute_url())


def detail(request, section, slug):
    """
    Renders a page
    """
    page = get_object_or_404(Page, section=section, slug=slug)

    return render_to_response("pages/detail.html", {
        "page": page,
    }, context_instance=RequestContext(request))
