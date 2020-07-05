from rest_framework import exceptions, serializers
from rest_framework.serializers import ModelSerializer
# from django import  forms
# from django.core.exceptions import ValidationError

from emsapp.models import User, Employee


class UserSerializer(serializers.Serializer):

        username = serializers.CharField(required=True,
                 max_length= 4,
                 min_length=2,
                 error_messages={
                     'required':'用户名不能为空',
                     'min_length': '用户名长度不够',
                     'max_length':'用户名不规范'},
                                   )

        real_name = serializers.CharField(required=True,
                 max_length= 4,
                 min_length=2,
                 error_messages={
                     'required':'real_name不能为空',
                     'min_length': 'real_name长度不够',
                     'max_length':'real_name不规范'},
                                    )
        password = serializers.CharField(
            required=True,
            max_length=8,
            min_length=3,
            error_messages={
                'required': '密码不能为空',
                'min_length': '密码长度不够',
                'max_length': '密码不规范'},

        )
        # pwds = serializers.CharField(max_length=8)

        def validate_username(self, value):
            # data=attrs.get('username')
            user_obj=User.objects.filter(username=value).first()
            if user_obj:
                raise exceptions.ValidationError('用户名已存在')
            return value

        # def validate(self, attrs):
        #     # 可以对前端发送的所有数据进行自定义校验
        #     # print(self, "当前实例所使用的反序列化器")
        #     password = attrs.get("password")
        #     pwds = attrs.pop("pwds")
        #     # 自定义规则  两次密码如果不一致  则无法保存
        #     if password != pwds:
        #         raise exceptions.ValidationError("两次密码不一致")
        #     return attrs
        def create(self, validated_data):
            # 方法中完成新增
            # print(validated_data)
            return User.objects.create(**validated_data)



class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        # pwds = serializers.CharField()
        fields="__all__"
        # fields=('username','real_name','password','gender','status','register_time','pwds')
        # 自定义校验规则
        extra_kwargs={
             'emp_name':{
                 'required':True,
                 'max_length': 4,
                 'min_length':2,
                 'error_messages':{
                     'required':'用户名不能为空',
                     'min_length': '用户名长度不够',
                     'max_length':'用户名不规范'
                 }
             },
            'salary': {
                'required': True,
                # 'max_length': 7,
                # 'min_length': 3,
                'error_messages': {
                    'required': '工资不能为空',
                    # 'min_length': '最低工资不能小于三位数',
                    # 'max_length': '最高工资不能大于七位数'
                }
            },
            'age': {
                'required': True,
                # 'max_length': 4,
                # 'min_length': 1,
                'error_messages': {
                    'required': '年龄必填',
                    # 'min_length': '最低年龄是一位数',
                    # 'max_length': '最高年龄是三位数'
                }
            },

        }

    # def validate(self, attrs):
    #     # 可以对前端发送的所有数据进行自定义校验
    #     # print(self, "当前实例所使用的反序列化器")
    #     print(attrs)
    #     pwd = attrs.get("password")
    #     # s=attrs.get('pwds')
    #     # print(s)
    #     re_pwd = attrs.pop("pwds")
    #     print(re_pwd)
    #     print(attrs)
    #     # 自定义规则  两次密码如果不一致  则无法保存
    #     if pwd != re_pwd:
    #         raise exceptions.ValidationError("两次密码不一致")
    #     return attrs






# class UserSerializer(serializers.Serializer):
#
#         username = serializers.CharField(required=True,
#                  max_length= 4,
#                  min_length=2,
#                  error_messages={
#                      'required':'用户名不能为空',
#                      'min_length': '用户名长度不够',
#                      'max_length':'用户名不规范'})
#         real_name = serializers.CharField(required=True,
#                  max_length= 4,
#                  min_length=2,
#                  error_messages={
#                      'required':'real_name不能为空',
#                      'min_length': 'real_name长度不够',
#                      'max_length':'real_name不规范'})
#         password = serializers.CharField(
#             required=True,
#             max_length=8,
#             min_length=3,
#             error_messages={
#                 'required': '密码不能为空',
#                 'min_length': '密码长度不够',
#                 'max_length': '密码不规范'}
#         )
#         pwds = serializers.CharField(max_length=8)


# def validate_username(self, value):
#     # data=attrs.get('username')
#     user_obj=User.objects.filter(username=value).first()
#     if user_obj:
#         raise exceptions.ValidationError('用户名已存在')
#     return value
#
# def validate(self, attrs):
#     # 可以对前端发送的所有数据进行自定义校验
#     # print(self, "当前实例所使用的反序列化器")
#     password = attrs.get("password")
#     # print(pwd)
#     pwds = attrs.pop("pwds")
#     # print(re_pwd)
#     # 自定义规则  两次密码如果不一致  则无法保存
#     if password != pwds:
#         raise exceptions.ValidationError("两次密码不一致")
#     return attrs
# def create(self, validated_data):
#     # 方法中完成新增
#     # print(validated_data)
#     return User.objects.create(**validated_data)
