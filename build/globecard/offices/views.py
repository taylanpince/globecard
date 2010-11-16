from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from offices.models import Office


def list(request):
    """
    Renders a list of offices
    """
    offices = Office.objects.all()

    return render_to_response("offices/list.html", {
        "offices": offices,
    }, context_instance=RequestContext(request))


def detail(request, slug):
    """
    Renders Location with the given slug
    """
    office = get_object_or_404(Office, slug=slug)

    return render_to_response("offices/detail.html", {
        "office": office,
    }, context_instance=RequestContext(request))
