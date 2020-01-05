from django.db import models
import uuid


class Music(models.Model):
    music = models.CharField(
        max_length=80
    )
    votes = models.IntegerField()


class Party(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    musics = models.ForeignKey(
        'Music',
        models.DO_NOTHING
    )
