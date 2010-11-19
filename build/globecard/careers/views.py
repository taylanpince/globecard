from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from careers.forms import JobApplicationForm
from careers.models import JobPosition


def landing(request):
    """
    Landing page for careers
    """
    return render_to_response("careers/landing.html", {
        
    }, context_instance=RequestContext(request))


def list(request):
    """
    Renders a list of available positions
    """
    positions = JobPosition.objects.all()

    return render_to_response("careers/list.html", {
        "positions": positions,
    }, context_instance=RequestContext(request))


def apply(request):
    """
    Renders an application form and handles it
    """
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("careers_apply_done"))
    else:
        form = JobApplicationForm()

    return render_to_response("careers/apply.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def apply_done(request):
    """
    Renders a thank you page
    """
    return render_to_response("careers/apply_done.html", {
        
    }, context_instance=RequestContext(request))
