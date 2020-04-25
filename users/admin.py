from django.contrib import admin
from . import models


@admin.register(models.User)  # Decorator
class CustomUserAdmin(admin.ModelAdmin):
    pass


# Decorator Alternative
# admin.site.register(models.User, CustomUserAdmin)
