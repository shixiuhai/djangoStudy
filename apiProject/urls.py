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
from django.urls import path, include
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
router.register(r'videoInformation', restFrameworkViews.VideoInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # can use for APIview
    # delete 删除
    # get 查询
    path(r'videoShow/',blogViews.VideoShow.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/',schema_view,name='docs'),


]
