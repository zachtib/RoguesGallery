from django.http import Http404
from django.shortcuts import render

from libraries.models import Library


def _get_library_or_404(library_id: str):
    try:
        return Library.objects.get_by_urlsafe_id(library_id)
    except Library.DoesNotExist:
        raise Http404("No library found for the given id")


def library_list(request):
    libraries = Library.objects.all()
    return render(request, "libraries/list.html", {
        "libraries": libraries,
    })


def library_detail(request, library_id):
    library = _get_library_or_404(library_id)
    return render(request, "libraries/detail.html", {
        "library": library,
    })
