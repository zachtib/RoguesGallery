from django.urls import path

from . import views

urlpatterns = [
    path("<str:library_id>/", views.player, name="player"),
    path("<str:library_id>/control", views.controller, name="controller"),
]
