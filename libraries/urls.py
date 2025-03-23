from django.urls import path

from . import views

urlpatterns = [
    path("", views.library_list, name="library-list"),
]
