from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class GalleryUser(AbstractUser):
    pass


class GalleryUserProfile(models.Model):
    user = models.OneToOneField(
        "users.GalleryUser",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Profile for {self.user}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


@receiver(post_save, sender=GalleryUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    GalleryUserProfile.objects.get_or_create(user=instance)
