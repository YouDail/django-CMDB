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


class Server(BaseModel):
    hostname = models.CharField(max_length=32, verbose_name="主机名")
    ip = models.CharField(max_length=32, verbose_name="ip")
    mac = models.CharField(max_length=32, verbose_name="物理地址")
    cpu = models.CharField(max_length=32, verbose_name="cpu")
    mem = models.CharField(max_length=32, verbose_name="内存")
    disk = models.CharField(max_length=32, verbose_name="磁盘")
    system = models.CharField(max_length=32, verbose_name="系统")
    io = models.CharField(max_length=32, verbose_name="IO")
    last_login_time = models.DateTimeField(verbose_name="上次登录时间")
    last_login_user = models.IntegerField(verbose_name="上次登录用户")
    is_active = models.CharField(max_length=32, verbose_name="是否被激活")

class UserServer(BaseModel):
    usr_id = models.IntegerField()
    ser_id = models.IntegerField()