# 最良心的 Python 教程推荐django教程Part 1 和Part2
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