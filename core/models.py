from django.db import models


class TimeStampModel(models.Model):

    """ Time stamp model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:  # Model doesn't go to database
        abstract = True
