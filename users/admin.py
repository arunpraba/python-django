from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # Decorator
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "gender", "language", "superhost")
    list_filter = ("gender", "language", "superhost")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


# Decorator Alternative
# admin.site.register(models.User, CustomUserAdmin)
