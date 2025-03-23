from django.shortcuts import render, get_object_or_404

from libraries.models import Library


def library_list(request):
    libraries = Library.objects.all()
    return render(request, "libraries/list.html", {
        "libraries": libraries,
    })


def library_details(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, "libraries/detail.html", {
        "library": library,
    })
