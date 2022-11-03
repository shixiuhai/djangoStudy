from rest_framework import serializers
from .models import VideoInformation,VideoDetail
from django.contrib.auth import get_user_model

class VideoInformationSerializer(serializers.ModelSerializer):
    video_time=serializers.SerializerMethodField()

    
    def get_video_time(self,instance):
        print('---')
        item_list=[]
        for item in VideoDetail.objects.filter(video_information_id=instance.id).all():
            item_list.append(item.video_time)
        return item_list

    class Meta:
        model = VideoInformation
        # fields = '__all__'
        # get video_time 
        fields = ('id','video_name','video_url','author','video_time')
        read_only_fields = ('id', 'author', 'video_name')