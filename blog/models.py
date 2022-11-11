from django.db import models

# Create your models here.

class VideoInformation(models.Model):
    id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'video_information'

class VideoDetail(models.Model):
    id = models.AutoField(primary_key=True)
    video_information_id = models.IntegerField(blank=True, null=True)
    video_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_detail'