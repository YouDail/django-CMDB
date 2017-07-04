# 用Django写的注册，验证登录部分：

### 注册

运行项目后，本地在浏览器中访问：`127.0.0.1:8000/users/register`

注册成功以后会自动跳转到登录页面

### 登陆

本地浏览器中访问：`127.0.0.1:8000/users/login`

登陆成功会自动跳转到Index页面

### 验证cookie

直接本地浏览器中访问：`127.0.0.1:8000/users/index`,如果cookie中存在已登录过的用户名，则验证通过；如果cookie中没有登录信息，会自动跳转到login页面让用户登录操作

<hr>
# 代码工作流程：

![](http://opbkao85k.bkt.clouddn.com/CMDB_framwork_flow.png)