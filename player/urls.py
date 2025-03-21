from django.urls import path

from . import views

urlpatterns = [
    path("<uuid:library_id>/", views.player, name="player"),
    path("<uuid:library_id>/control", views.controller, name="controller"),
]
