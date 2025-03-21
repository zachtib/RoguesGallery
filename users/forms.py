from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import GalleryUser


class GalleryUserCreationForm(UserCreationForm):
    class Meta:
        model = GalleryUser
        fields = ("username", "email")


class GalleryUserChangeForm(UserChangeForm):
    class Meta:
        model = GalleryUser
        fields = ("username", "email")
