from django.urls import path

from . import views

urlpatterns = [
    path("", views.library_list, name="library-list"),
    path("<str:library_id>/", views.library_detail, name="library-detail"),
]
