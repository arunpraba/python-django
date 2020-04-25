from django.db import models


class TimeStampModel(models.Model):

    """ Time stamp model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # Model doesn't go to database
        abstract = True
