from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation admin definition """

    list_display = (
        "__str__",
        "guest",
        "check_in",
        "check_out",
        "status",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
