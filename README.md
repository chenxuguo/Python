# Python
最良心的 Python 教程：
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
