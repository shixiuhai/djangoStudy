from rest_framework import serializers
from .models import VideoInformation
from django.contrib.auth import get_user_model
class VideoInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInformation
        fields = '__all__'
        # fields = ('id','video_name','video_url','author')

        read_only_fields = ('id', 'author', 'video_name')