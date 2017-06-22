# coding:utf-8
from django.db import models

class BaseModel(models.Model):
    delete_Flag = models.CharField(max_length=32, verbose_name="删除标志")

class User(BaseModel):
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    city = models.CharField(max_length=32, verbose_name="城市")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length=32, verbose_name="电话")

class Group(BaseModel):
    name = models.CharField(max_length=32, verbose_name="组名")
    description = models.TextField(verbose_name="组描述")

class Permission(BaseModel):
    name = models.CharField(max_length=32, verbose_name="权限名称")
    description = models.TextField(verbose_name="权限描述")

class UserGroup(BaseModel):
    user_id = models.IntegerField(verbose_name="用户ID")
    group_id = models.IntegerField(verbose_name="组ID")

class UserPermission(BaseModel):
    user_id = models.IntegerField(verbose_name="用户ID")
    permission_id = models.IntegerField(verbose_name="权限ID")

class PermissionGroup(BaseModel):
    permission_id = models.IntegerField(verbose_name="权限ID")
    group_id = models.IntegerField(verbose_name="组ID")