from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView

from emsapp import models
from emsapp.models import User, Employee
from emsapp.serializers import UserSerializer, EmployeeSerializer
from utils.response import ApiResponse


class RegisterAPIView(APIView,CreateModelMixin):
    # 注册请求逻辑处理
    def post(self,request,*args,**kwargs):
        data=request.data
        # print(data)
        resu=UserSerializer(data=data)
        # t=resu.pop('pwds')
        # print(resu)
        resu.is_valid(raise_exception=True)
        obj=resu.save()
        # return ApiResponse('ok')
        return ApiResponse(200,True,result=UserSerializer(obj).data)
    def get(self,request,*args,**kwargs):
        username=request.query_params.get('username')
        password=request.query_params.get('password')
        resu=User.objects.filter(username=username,password=password).first()
        if resu:
            data=UserSerializer(resu).data
            return ApiResponse(200,True,result=data)
        return ApiResponse(400,False)
#查询员工信息返回页面
class EmpView(ListModelMixin,GenericAPIView,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"
    def get(self,request,*args,**kwargs):
        print(kwargs.get('id'))
        if 'id' in kwargs:
            bt=self.retrieve(request,*args,**kwargs)
            return ApiResponse(200,True,result=bt.data)
        else:
            data=self.list(request,*args,**kwargs)
            return ApiResponse(200,True,result=data.data)
    def post(self,request,*args,**kwargs):
        data=self.create(request,*args,**kwargs)
        return ApiResponse(200,True,result=data.data)

    # def delete(self, request, *args, **kwargs):
    #     data=request.data.get('id')
    #     models.Employee.objects.filter(pk=data).delete()
    #     return ApiResponse(http_status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        data=request.data
        print(data)
        response = self.partial_update(request, *args, **kwargs)
        return ApiResponse(results=response.data)
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return ApiResponse(http_status=status.HTTP_204_NO_CONTENT)

