from django.shortcuts import render, get_object_or_404

from libraries.models import Library


def player(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, "player/player.html", {
        "library_id": library_id,
        "library": library,
    })


def controller(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, "player/controller.html", {
        "library_id": library_id,
        "library": library,
    })
