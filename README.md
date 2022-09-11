# 最良心的 Python 教程推荐django教程Part 1 和Part2

## 安装虚拟环境
```dos
pip install virtualenv
```
进入虚拟环境
```dos
virtualenv venv -p python3
venv/Scripts/activate.bat
```
如果你在命令行的前面看到 （venv），就说明，虚拟环境激活成功，现在已经进入到虚拟环境里面了。
在虚拟环境下安装需要的软件包
```bash
pip install django==1.11 
```
或者
```bash
pip install -r requirements.txt
```
将Django的例子敲了一遍， 使用starUML将图画了一遍
刚开始starUML已经不能下载文件，今天重新试了。[下载地址](https://staruml.io/download/releases-v5/StarUML%20Setup%205.0.2.exe)
代码中有两处需要修改:
## 1.表格标题变黑 
<thead class='thead-inverse'>  改为
<thead class="thead-dark">
## 2.网页路径
myproject 使用的是^$正则表达式，它将匹配空白路径，这是主页（此URL：**http://127.0.0.1:8000**）。
如果我想匹配URL **http://127.0.0.1:8000/homepage/**，那么我们 url 的正则表达式就应该这样写：
url(r'^homepage/$', views.home, name='home')。

myproject urls.py
```python
urlpatterns = [
    url(r'^$', views.home, name='home'), // 原文在这里有乱码r''^code/
    url(r'^admin/', admin.site.urls),
]
```
hellodajiano urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', show_index),
]
```
# Part 2
The second association between Post and User is a direct association 
(see the arrow at the end of the line), meaning we are interested only 
in one side of the relationship which is what User has edited a given Post. 

Every Django model comes with a special attribute; we call it a Model Manager.
You can access it via the Python attribute objects

# Part 3
which is not very sustainable in the long run. It’s also a bad practice.
Being in control is important because it let us write code with more confidence. 

The reason why we used board.topics.all instead of just board.topics is because 
board.topics is a Related Manager, which is pretty much similar to a Model Manager, 
usually available on the board.objects property.

Data validation should always be done on the server side, where we have full control over the data.

As usual, we also implement several test cases. That’s how we develop with confidence.

# Part 4
In the next tutorial, we are going to learn everything about authentication and how to protect our views 
and resources.[link](https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html)

用django-admin startapp account报错,要用
python django-admin.py startapp account

test_view_password_reset.py中下面两种代码测试都是成功的
```python
self.assertContains(self.response, '<input', 5)
```
should be
```python
self.assertContains(self.response,'input', 5)
```
but we still have to test the form itself. Instead of just keep adding tests to the accounts/tests.py file,
let’s improve the project design a little bit.

we don’t need to be an expert in regular expressions. It’s just a matter of knowing the common ones.

They make use of a view decorator named @login_required. This decorator prevents non-authorized users to access this page.

The refresh_from_db() method make sure we have the latest state of the data.

# Part5
Here we have 11 posts. But not all of them belongs to the “Django” board.

Migration is a fundamental part of Web development with Django.

The makemigrations command automatically generated the 0003_topic_views.py file,


在views.py增加页面浏览次数
```python
+    topic.views += 1
+    topic.save()
```
但是要先在模型中增加views字段
```python
views = models.PositiveIntegerField(default=0)
```
增加字段后，还要把数据库给修改
```dos
python manage.py makemigrations
python manage.py migrate
```

# Part6
 the handling of HTTP methods are done in separate methods, rather than using condi
 tional branching, and there are also the Generic Class-Based Views (GCBV).