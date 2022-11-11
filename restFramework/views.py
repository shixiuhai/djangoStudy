from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

# Create your views here.
# import model
from .models import VideoInformation
# import serializers
from .serializers import VideoInformationSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


# list() 提供一组数据
# retrieve() 提供单个数据
# create() 创建数据
# update() 保存数据
# destory() 删除数据
class VideoInformationViewSet(viewsets.ModelViewSet):
    queryset = VideoInformation.objects.all()
    serializer_class = VideoInformationSerializer
    pagination_class = CustomPagination
     
    
