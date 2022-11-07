from rest_framework import serializers
from .models import VideoInformation,VideoDetail
from django.contrib.auth import get_user_model
class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoDetail
        fields='__all__'

class VideoInformationSerializer(serializers.ModelSerializer):
    # # 视频详情序列化对象
    # VideoDetailSerializer=VideoDetailSerializer()
    # get for videoDetailTable
    video_time=serializers.SerializerMethodField()
    class Meta:
        model = VideoInformation
        # fields = '__all__'
        # get video_time 
        fields = ('id','video_name','video_url','author','video_time')
        # read_only_fields = ('id',)

    # select data
    def get_video_time(self,instance):
        item_list=[]
        for item in VideoDetail.objects.filter(video_information_id=instance.id).all():
            item_list.append(item.video_time)
        return item_list

    # crate data
    def create(self,validated_data):
        # print('---')
        # print(validated_data)
        # # 去除提交的关于videoDetail表的信息
        # video_time=validated_data["video_time"]
        # print(video_time)
        # print('+++')
        # videoInformationData=validated_data.pop('video_time')
        # # 保存电影基本信息
        id=VideoInformation.objects.create(**validated_data).id
        print("----")
        print(VideoInformation)
        # print(object.id)
        # print("++++++")
        # # 保存详细信息到videoDetail表
        # VideoDetail.objects.create(video_information_id=id,video_time=video_time)
        return id

    

    