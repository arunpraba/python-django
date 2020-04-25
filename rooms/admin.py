from django.contrib import admin
from . import models


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    # list_display = (
    #     "name",
    #     "description",
    #     "country",
    #     "price",
    #     "address",
    #     "guests",
    #     "beds",
    #     "bedrooms",
    #     "baths",
    #     "check_in",
    #     "check_out",
    #     "instant_book",
    #     "host",
    # )
    pass
