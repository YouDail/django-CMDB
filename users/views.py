#coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from .models import User
import hashlib
from django.http import JsonResponse


def repeat_user(username):
    '''
    完成用户名查重功能
    :param username:
    :return:
    '''
    status = {"status":"","result":""}
    try:
        user_data = User.objects.get(username = username)
        status["status"] = "success"
        #status["result"] = user_data
    except Exception as e:
        status["status"] = "error"
    return status

def hash_password(password):
    '''
    md5密码加密
    :param password:
    :return:
    '''
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def register_repeat(request):
    if request.method == "POST" and request.POST:
        name = request.POST["username"]
        return JsonResponse(repeat_user(name))
    else:
        return JsonResponse({"status":"","result":""})


def register(request):
    if request.method == "POST" and request.POST:
        name = request.POST["Username"]
        passwd = request.POST["Password"]

        #给密码hash加密
        passwd = hash_password(passwd)

        #新注册的用户数据入库
        user = User()
        user.username = name
        user.password = passwd
        user.save()

        return HttpResponseRedirect("/users/login")

    return render(request, 'register.html', locals())

def loginValid(func):
    def inner(request, *args, **kwargs):
        name = request.COOKIES.get("name")  #获取cookie
        if not name:
            return HttpResponseRedirect("login")
        return func(request, *args, **kwargs)
    return inner

def login(request):
    if request.method == "POST" and request.POST:
        name = request.POST["Username"]
        passWd = request.POST["Password"]
        passWd = hash_password(passWd)

        #验证用户名和密码是否存在
        if (repeat_user(name)["status"] == "success"):
            dbPassWord = User.objects.get(username = name).password
            if passWd == dbPassWord:
                response = HttpResponseRedirect("index")
                response.set_cookie('name', name, max_age= 360)
                request.session["name"] = name
                return response
            else:
                return render(request, "login.html", locals())
        else:
            return  render(request, "login.html", locals())

    return render(request, 'login.html', locals())

@loginValid
def index(request):
    return render(request, 'index.html' , locals())
