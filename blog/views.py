import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import VideoInformation
from .serializers import VideoInformationSerializer
from rest_framework.pagination import PageNumberPagination
import json
class CustomPagination(PageNumberPagination):
    page_size = 2 # 默认每页显示的多少条记录
    page_query_param = 'page'  # URL中页码的参数
    page_size_query_param = 'size' # # URL中每页显示条数的参数
    max_page_size = 10000 # 后台控制显示的最大记录条数，防止用户输入的查询条数过大

# Create your views here.
class VideoShow(APIView):
    def get(self, request, format=None):
        # get all information for database
        a= VideoInformation.objects.filter(id=1)
        page =CustomPagination()  # 产生一个分页器对z
        print(request.data)
        ret = page.paginate_queryset(a,request)
        # use serializer
        serializer = VideoInformationSerializer(ret,many=True)
        return Response(serializer.data)

    # def post(self,request):
    #     pass
    # def put(self,request):
    #     pass
    # def delete(self,request):
    #     pass