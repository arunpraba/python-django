from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin definition """

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
