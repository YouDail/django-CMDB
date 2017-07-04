#coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from .models import User
import hashlib
from django.http import JsonResponse

'''
登陆用户名验证
'''
def loginValid(func):
    def inner(request, *args, **kwargs):
        name = request.COOKIES.get("name")  #获取cookie
        if not name:
            return HttpResponseRedirect("/users/login")
        return func(request, *args, **kwargs)
    return inner

def repeat_user(username):
    '''
    完成用户名查重功能
    :param username:
    :return:
    '''
    status = {"status":""}
    if User.objects.filter(username = username):
        status["status"] = "success"
    else:
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
        #新建一个用户模型
        u = User()
        #缓存用户POST上来的数据
        u.username = request.POST["Username"]
        u.password = hash_password(request.POST["Password"])  #密码加密入库
        u.city = request.POST["City"]
        u.email = request.POST["Email"]
        u.phone = request.POST["Phone"]
        #保存到数据库
        u.save()
        return render(request, "login.html", locals())
    return render(request, 'register.html', locals())

def login(request):
    global referer
    if request.method == "POST" and request.POST:
        name = request.POST["Username"]
        passWd = request.POST["Password"]
        passWd = hash_password(passWd)

        #验证用户名和密码是否存在
        if (repeat_user(name)["status"] == "success"):
            dbPassWord = User.objects.get(username = name).password
            if passWd == dbPassWord:
                response = HttpResponseRedirect("/users/index")
                response.set_cookie('name', name, max_age= 3600)
                request.session["name"] =    name
                return response
            else:
                password_warnning = "Wrong password!"
                return render(request, "login.html", locals())
        else:
            username_warnning = "Username not exist."
            return  render(request, "login.html", locals())
    print(request.META.get('HTTP_REFERER'))
    return render(request, 'login.html', locals())


@loginValid
def index(request):
    user_name = request.COOKIES.get("name","")
    return render(request, 'index.html', locals())

@loginValid
def userlist(req):
    return render(req, 'tables.html', locals())
