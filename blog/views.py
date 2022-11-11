from asyncio.log import logger
import json
from venv import create
from rest_framework.permissions import AllowAny,IsAuthenticated
# swagger
import coreapi
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView, Response

from .models import VideoDetail, VideoInformation
from .serializers import VideoDetailSerializer, VideoInformationSerializer

# 导入日志包
import logging
logger = logging.getLogger('django')
class CustomPagination(PageNumberPagination):
    page_size = 2 # 默认每页显示的多少条记录
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size' # # URL中每页显示条数的参数
    max_page_size = 10000 # 后台控制显示的最大记录条数，防止用户输入的查询条数过大


class VideoDetailAPI(APIView):
    def get(self,request,pk1,pk2):
        print('++++++')
        print(pk1,pk2)
        print('++++++')
        return Response(pk1)
# Create your views here.
class VideoShow(APIView):
    # 设置认证类
    permission_classes=[AllowAny
    ]
    # 参数测试
    # schema = AutoSchema()
    def get(self,request,pk):
        """
        单一修改接口
        """
        a= VideoInformation.objects.filter(id=pk)
        # page =CustomPagination()  # 产生一个分页器对
        # print(request.data)
        # ret = page.paginate_queryset(a,request)
        # print(ret)
        # use serializer
        # serializer = VideoInformationSerializer(instance=ret,many=True)
        serializer = VideoInformationSerializer(instance=a,many=True)
        return Response(serializer.data)


    def post(self,request):
        logger.info('heelo word')
        # print(request.data)
        # 使用序列号器接收对象
        serializer = VideoInformationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response("添加视频信息错误")
        # 保存数据
        serializer.save()
        # 保存到 id到videoDetail
        video_information_id=serializer.data.get('id')
        # print(type(request.data))
        detail_serializer= VideoDetailSerializer(data={'video_information_id':video_information_id})
        if not detail_serializer.is_valid():
            return Response("添加用户详情错误")
        detail_serializer.save()
        # 重写查询一遍 方案1
        # video_information=VideoInformation.objects.filter(id=video_information_id)
        # serializer=VideoInformationSerializer(instance=video_information,many=True)
        
        # video_detail=VideoDetail.objects.filter(video_information_id=161)
        # serializer=VideoDetailSerializer(instance=video_detail,many=True)
        # print(serializer.data)
        # 方案二
        # serializer=serializer.get_video_detail(instance=)

        return_data=serializer.data
        return_data["video_detail"]=[detail_serializer.data]
        # serializer.data['video_detail']=[detail_serializer.data]
        # serializer.data['video_detail']=['nihao1']
        # # 返回信息添加上详情信息
        # videoDetailObj=VideoDetail.objects.filter(video_information_id=video_information_id)
        # # print(videoDetailObj)
        # serializer.data['video_detail']=VideoDetailSerializer(instance=videoDetailObj,many=True).data
        # print(r)
        # return Response(serializer.data)
        return Response(return_data)

    # def delete(self,request):
    def delete(self,request,pk):
    
        """
        这是删除接口参数
        传参 /
        """
        # pk=request.query_params.dict()['pk']
        print(pk)
        print('----')
    
        return Response("sucessrul")

# schema = ManualSchema(
#             fields=[
#                 coreapi.Field(
#                     name="username",
#                     required=True,
#                     location='form',
#                     schema=coreschema.String(
#                         title="Username",
#                         description="Valid username for authentication",
#                     ),
#                 ),
#                 coreapi.Field(
#                     name="password",
#                     required=True,
#                     location='form',
#                     schema=coreschema.String(
#                         title="Password",
#                         description="Valid password for authentication",
#                     ),
#                 ),
#             ],
#             encoding="application/json",
#         )