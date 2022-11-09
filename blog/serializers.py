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
    # name = serializers.CharField(min_length=3,max_length=20)               # 显示普通字段
    # ut = serializers.CharField(source='ut.type_name',required=False)       # 显示一对多字段名称
    # gp = serializers.SerializerMethodField(read_only=True)                 # 自定义显示（显示多对多）
    # xxx = serializers.
    # (source='name',required=False)              # 也可以自定义显示字段名称
    # ut_id = serializers.IntegerField(write_only=True)                   

    # get for videoDetailTable
    # video_time=serializers.SerializerMethodField()
    video_detail=serializers.SerializerMethodField()
    # video_time=serializers.CharField(label='电影发布时间',default='123')
    class Meta:
        model = VideoInformation
        # fields = '__all__'
        # get video_time 
        fields = ('id','video_name','video_url','author','video_detail')
    
    # select data and get detail
    def get_video_detail(self,instance):
        # 获取信息
        video_detail=VideoDetail.objects.filter(video_information_id=instance.id).all()
        serializers=VideoDetailSerializer(video_detail,many=True)
        print(serializers.data)


        return serializers.data
    # crate data
    def create(self,validated_data):
        videoInformation=VideoInformation(**validated_data)
        videoInformation.save()
        return validated_data
    
    # update data
    def update(self,instance, validated_data):
        pass


    

    