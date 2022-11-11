from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from django_redis import get_redis_connection
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebTok

from .models import User
from .serializers import (CreateUserSerializer, EmailSerializer,
                          UserDetailSerializer)

# Create your views here.


class UserView(CreateAPIView):
    """用户注册"""
    # 指定序列化器
    serializer_class = CreateUserSerializer





class UsernameCountView(APIView):
    """判断用户是否已注册"""

    def get(self, request, username):
        # 查询user表
        count = User.objects.filter(username=username).count()

        # 包装响应数据
        data = {
            'username': username,
            'count': count
        }
        # 响应
        return Response(data)


class MobileCountView(APIView):
    """判断手机号是否已注册"""

    def get(self, request, mobile):
        # 查询数据库
        count = User.objects.filter(mobile=mobile).count()
        # 构造响应数据
        data = {
            'mobile': mobile,
            'count': count
        }
        # 响应
        return Response(data)


# GET /user/
class UserDetailView(RetrieveAPIView):
    """用户详细信息展示"""
    serializer_class = UserDetailSerializer
    # queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # 指定权限,只有通过认证的用户才能访问当前视图

    def get_object(self):
        """重写此方法返回 要展示的用户模型对象"""
        return self.request.user


# PUT /email/
class EmailView(UpdateAPIView):
    """更新用户邮箱"""
    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer

    def get_object(self):
        return self.request.user


class EmailVerifyView(APIView):
    """激活用户邮箱"""

    def get(self, request):
        # 获取前端查询字符串中传入的token
        token = request.query_params.get('token')
        if not token:
            return Response({'message': '缺少token'}, status=status.HTTP_400_BAD_REQUEST)

        # 把token解密 并查询对应的user
        user = User.check_verify_email_token(token)
        # 修改当前user的email_active为True
        if user is None:
            return Response({'message': '激活失败'}, status=status.HTTP_400_BAD_REQUEST)
        user.email_active = True
        user.save()
        # 响应
        return Response({'message': 'ok'})


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

class UserAuthorizeView(ObtainJSONWebToken):
    """自定义账号密码登录视图,实现购物车登录合并"""

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            # 账号登录时合并购物车
            # merge_cart_cookie_to_redis(request, user, response)

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



   



