import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from roguesgallery import settings


class LibraryManager(models.Manager):

    def get_by_urlsafe_id(self, urlsafe_id: str):
        decoded_id = uuid.UUID(bytes=urlsafe_base64_decode(urlsafe_id))
        return self.get(id=decoded_id)


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

    def get_urlsafe_id(self):
        return urlsafe_base64_encode(self.id.bytes)

    class Meta:
        verbose_name_plural = "Libraries"
