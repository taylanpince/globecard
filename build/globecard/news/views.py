from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from news.models import NewsEntry


NEWS_ENTRIES_PER_PAGE = 5


def list(request):
    """
    Renders a list of news entries
    """
    entries = NewsEntry.objects.all()
    paginator = Paginator(entries, NEWS_ENTRIES_PER_PAGE)

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)

    return render_to_response("news/list.html", {
        "entries": entries,
    }, context_instance=RequestContext(request))


def detail(request, slug):
    """
    Renders a NewsEntry with the given slug
    """
    entry = get_object_or_404(NewsEntry, slug=slug)

    return render_to_response("news/detail.html", {
        "entry": entry,
    }, context_instance=RequestContext(request))
