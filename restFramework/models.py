from django.db import models

# Create your models here.
class VideoInformation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    video_name = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'video_information'


