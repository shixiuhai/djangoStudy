import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import VideoInformation,VideoDetail
from .serializers import VideoInformationSerializer
from rest_framework.pagination import PageNumberPagination
import json
# swagger
import coreapi
from rest_framework.schemas import AutoSchema
class CustomPagination(PageNumberPagination):
    page_size = 2 # 默认每页显示的多少条记录
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size' # # URL中每页显示条数的参数
    max_page_size = 10000 # 后台控制显示的最大记录条数，防止用户输入的查询条数过大

# Create your views here.
class VideoShow(APIView):
    # 参数测试
    
    def get(self,request,pk)->object:
        """
        get 接口
        """
        # schema= AutoSchema(
        #     manual_fields=[
        #         coreapi.Field(name='pk',required=True,location='query',description='主键',type='string')
        #     ]
        # )
        
        # a=request.query_params.dict()['page']
        # b=request.query_params.dict()['size']
        # print(a['page'],a['size'])
        # get all information for database
        a= VideoInformation.objects.filter(id=1)
        page =CustomPagination()  # 产生一个分页器对
        print(request.data)
        ret = page.paginate_queryset(a,request)
        print(ret)
        # use serializer
        serializer = VideoInformationSerializer(instance=ret,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # print(request.data)
        # 使用序列号器接收对象
        serializer = VideoInformationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response("出现错误")
        # 保存数据
        serializer.save()
        print(serializer)
        print('+++')
        return Response(serializer.data)

    def delete(self,request,pk):
        """
        这是删除接口参数
        """
        chema=None
        print('----')
        # print(p1)
    # def post(self,request):
    #     pass
    # def put(self,request):
    #     pass
    # def delete(self,request,pk):
    #     print('---')
    #     print(pk)
    #     print('---')
    #     return Response("sucessful")

    #     # pk_list=pk.split(',')
        # print(pk_list)
        return Response("sucessrul")