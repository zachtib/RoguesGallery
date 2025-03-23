import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from roguesgallery import settings


class LibraryManager(models.Manager):

    def get_by_urlsafe_id(self, urlsafe_id: str):
        decoded_id = uuid.UUID(bytes=urlsafe_base64_decode(urlsafe_id))
        return self.get(id=decoded_id)

    def get_by_urlsafe_id_or_404(self, urlsafe_id: str):
        try:
            return self.get_by_urlsafe_id(urlsafe_id)
        except Library.DoesNotExist:
            from django.http import Http404
            raise Http404("No library found for the given id")


class Library(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = LibraryManager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("library-detail", kwargs={
            "library_id": self.get_urlsafe_id(),
        })

    def get_player_url(self):
        from django.urls import reverse
        return reverse("player", kwargs={
            "library_id": self.get_urlsafe_id(),
        })

    def get_controller_url(self):
        from django.urls import reverse
        return reverse("controller", kwargs={
            "library_id": self.get_urlsafe_id(),
        })

    def get_urlsafe_id(self):
        return urlsafe_base64_encode(self.id.bytes)

    class Meta:
        verbose_name_plural = "Libraries"
