from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import GalleryUserCreationForm, GalleryUserChangeForm
from .models import GalleryUser, GalleryUserProfile


class GalleryUserProfileInline(admin.StackedInline):
    model = GalleryUserProfile
    can_delete = False
    verbose_name_plural = "User Profile"


class GalleryUserAdmin(UserAdmin):
    add_form = GalleryUserCreationForm
    form = GalleryUserChangeForm
    model = GalleryUser
    list_display = [
        "email",
        "username",
    ]
    inlines = [GalleryUserProfileInline]


admin.site.register(GalleryUser, GalleryUserAdmin)
admin.site.register(GalleryUserProfile)
