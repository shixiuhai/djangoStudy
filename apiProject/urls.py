"""apiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import routers
# import restFramework app views
from restFramework import views as restFrameworkViews
# import blog app views
from blog import views as blogViews
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# create router object
router = routers.DefaultRouter()

schema_view = get_schema_view(title='API文档', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
# only for viewset
router.register(r'videoInformation', restFrameworkViews.VideoInformationViewSet,)

"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录
APIView  序列化器
"""
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # can use for APIview
    # delete 删除
    # get 查询
    # post put请求
    # path(r'videoShow',blogViews.VideoShow.as_view()),
    # get delete 请求
    # path(r'videoShow/<pk>',blogViews.VideoShow.as_view()),
    # 整体查询 get
    # 查询单一 修改 删除
    # 列表视图的路由APIView
    # url(r'^books/$', views.BookListAPIView.as_view()),
    # # 详情视图的路由APIView
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view()),
    # path('videoShow',blogViews.VideoShow.as_view()),
    re_path(r'^videoShow/$', blogViews.VideoShow.as_view()),
    re_path(r'^videoShow/(?P<pk>\d+)/$', blogViews.VideoShow.as_view()),
    re_path(r'^test/(?P<pk1>\d+)/(?P<pk2>\d+)/$', blogViews.VideoDetailAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/',schema_view,name='docs'),
]
