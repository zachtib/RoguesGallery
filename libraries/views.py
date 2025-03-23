from django.shortcuts import render

from libraries.models import Library


def library_list(request):
    libraries = Library.objects.all()
    return render(request, "libraries/list.html", {
        "libraries": libraries,
    })


def library_detail(request, library_id):
    library = Library.objects.get_by_urlsafe_id_or_404(library_id)
    return render(request, "libraries/detail.html", {
        "library": library,
    })
