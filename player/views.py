from django.shortcuts import render

from libraries.models import Library


def player(request, library_id):
    library = Library.objects.get_by_urlsafe_id_or_404(library_id)
    return render(request, "player/player.html", {
        "library_id": library_id,
        "library": library,
    })


def controller(request, library_id):
    library = Library.objects.get_by_urlsafe_id_or_404(library_id)
    return render(request, "player/controller.html", {
        "library_id": library_id,
        "library": library,
    })
