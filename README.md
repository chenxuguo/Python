# 最良心的 Python 教程推荐django教程Part 1 和Part2

## 安装虚拟环境


```dos
python --version   # make sure the version is 3.6, or modify environment bin to python36
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

This is our first form. It’s a ModelForm associated with the Topic model. 

This is how we use the forms in a view.
```python
if request.method == 'POST':
    form = NewTopicForm(request.POST)
    if form.is_valid():
        topic = form.save()
        return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'form' : form})
```
When working with Bootstrap or any other Front-End library, I like to use a Django 
package called django-widget-tweaks. It gives us more control over the rendering 
process, keeping the defaults and just adding extra customizations on top of it.

Now to implement the Bootstrap 4 validation tags, we can change the new_topic.html template

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
CBVs are great to extend and reuse code.

 the handling of HTTP methods are done in separate methods, rather than using condi
 tional branching, and there are also the Generic Class-Based Views (GCBV).
 
Just like we did with the form.html partial template, we can also create something 
similar for the pagination HTML snippet.

Maybe you have already noticed, but there’s a small issue when someone replies to a 
post. It’s not updating the last_update field, so the ordering of the topics is broken right now.

# Intermediate Python

## format语句
 
C style
```c

	x, y = 1, 2
	print('%dx%d=%2d' % (x,y, x*y))
	print(f'{x}x{y}={x * y}' )
	print('{}x{}={}'.format(x, y, x *y))

	1X2=2
```

打印9 * 9 乘法表

```python

print('\n'.join([' '.join  ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))
 [f'{x}*{y+1}={x*(y+1)}' for x in range(1, 10) for y in range(0, x)]

1x1= 1
1x2= 2 2x2= 4
1x3= 3 2x3= 6 3x3= 9
1x4= 4 2x4= 8 3x4=12 4x4=16
1x5= 5 2x5=10 3x5=15 4x5=20 5x5=25
1x6= 6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36
1x7= 7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49
1x8= 8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64
1x9= 9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81

[f'{x}*{y+1}={x*(y+1)}' for x in range(1, 10) for y in range(0, x)]

['1*1=1', 
2*1=2', '2*2=4', 
'3*1=3', '3*2=6', '3*3=9', 
'4*1=4', '4*2=8', '4*3=12', '4*4=16',
'5*1=5', '5*2=10', '5*3=15', '5*4=20', '5*5=25', 
'6*1=6', '6*2=12', '6*3=18', '6*4=24', '6*5=30', '6*6=36', 
'7*1=7', '7*2=14', '7*3=21', '7*4=28', '7*5=35', '7*6=42', '7*7=49', 
'8*1=8', '8*2=16', '8*3=24', '8*4=32', '8*5=40', '8*6=48', '8*7=56', '8*8=64', 
'9*1=9', '9*2=18', '9*3=27', '9*4=36', '9*5=45', '9*6=54', '9*7=63', '9*8=72', '9*9=81']
```

## kwargs
```python
def test_args_kwargs(arg1, arg2, arg3 ):
    print("arg1:", arg1)
  	print("arg2:", arg2)
    print("arg3:", arg3)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3

```

## pdb

python -m pdb my_script.py

c: 继续执行
w: 显示当前正在执行的代码行的上下文信息
a: 打印当前函数的参数列表
s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

## Iterable

Iterable: 定义了可以返回一个迭代器的 __iter__ 方法，或者定义了可以支持下标索引的 __getitem__ 方法

Iteration: 定义了 next（Python2） 或者 __next__ 方法

## map

我们要把列表中所有元素一个个地传递给一个函数，并收集输出
```python

items = [1,2,3,4,5]
list(map(lambda x : x * x, items))

[2,4,9,16,25]
```

```python
def map1(func, list):
    for item in list:
         yield(func(item))
```

## Filter
filter 过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表
    ```python
		
	
	number_list = range(-5, 5)
	 less_than_zero = filter(lambda x: x < 0, number_list)
	 list(less_than_zero)
	[-5, -4, -3, -2, -1]
	```

## Reduce
	
当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数。
    ```python
	
	from functools import reduce
	product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

	# Output: 24

	

## Set
	
与列表（list）的行为类似，区别在于 set 不能包含重复的值
	`python

	some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
	
	duplicates = set([x for x in some_list if some_list.count(x) > 1])
	print(duplicates)
	
### Intersection
	valid = set(['yellow', 'red', 'blue', 'green', 'black'])
	input_set + set['red', 'brown'])
	print(input_set.intersection(valid))
	### output: set(['red'])

## 三元运算
	
三元运算符通常在Python里被称为条件表达式，这些表达式基于真（true）/假（false）的条件判断
	
True 等于1，而 False 等于0
	
	`python
	
	fat = True
	fitness = ('skinny', 'fat')[fat]

	# output: Ali is fat

	
## Property
他们是修改其他函数的功能的函数
	def hi(name='yasoob')
		return "hi " + name

	# output: 'hi yasoob'

在一个函数中定义另一个函数
	def hi(name='yasoob')
		print('now you are inside the hi() function')
	
		def greet():
			return 'now you are in the greet(0 function

		def welcome():
			return "now you are in the welcome() function"

		print(greet())
		print("welcome())
		print('now you are back in the hi() dfunction")

	#output:now you are inside the hi() function
	#       now you are in the greet() function
	#       now you are in the welcome() function
	#       now you are back in the hi() function

welcome() 在函数外不能调用
hi.welcome()也不行

不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来
	def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

	a = hi()
	print(a)
	#outputs: <function greet at 0x7f2143c01500>

	print(a())
	#outputs: now you are in the greet() function


将函数作为参数传给另一个函数

	def hi():
	    return "hi yasoob!"
	
	def doSomethingBeforeHi(func):
	    print("I am doing some boring work before executing hi()")
	    print(func())
	
	doSomethingBeforeHi(hi)
	#outputs:I am doing some boring work before executing hi()
	#        hi yasoob!

我们修改下上一个装饰器，并编写一个稍微更有用点的程序

    def a_new_decoration(a_func):
		
		def wrapTheFunction():
			print(I am doing some boring work before executing a_func()")

        	a_func()

        	print("I am doing some boring work after executing a_func()")

		return wrapTheFunction()

	def a_function_requiring_decoration():
		print("I'm the fucnction which need some decoration to remove my soul smell")


	a_function_requiring_decoration()
	
	#outputs:I am doing some boring work before executing a_func()
	#        I am the function which needs some decoration to remove my foul smell
	#        I am doing some boring work after executing a_func()

functools.wraps(func)

	def a_new_decorator(a_func):
    	def wraps(a_func):
			def wrapTheFunction():
		        print("I am doing some boring work ")
	                a_func()
	                print("I'm doing some boring work after")
		     wrapTheFunction.__name__ = a_func.__name__
        return wrapTheFunction
     return wraps(a_func)
	

@wraps 接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

日志是装饰器运用的另一个亮点
	from functools import wraps

	def logit(func):
        @wraps(func)
    	def with_logging(*args, **kwargs):
       		 print(func.__name__ + " was called")
       		 return func(*args, **kwargs)
   		return with_logging

	@logit
	def addition_func(x):
		"""Do some math."""
		return x + x

	result = addition_func(4)
	# Output: addition_func was called

让我们指定一个用于输出的日志文件
	from functools import wraps

	def logit(logfile='out.log'):
    	def logging_decorator(func):
        	@wraps(func)
        	def wrapped_function(*args, **kwargs):
            	log_string = func.__name__ + " was called"
            	print(log_string)
            	# 打开logfile，并写入内容
            	with open(logfile, 'a') as opened_file:
                	# 现在将日志打到指定的logfile
                	opened_file.write(log_string + '\n')
            	return func(*args, **kwargs)
        	return wrapped_function
    	return logging_decorator

	@logit()
	def myfunc1():
	    pass
	
	myfunc1()
	# Output: myfunc1 was called
	# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串


	@logit(logfile='func2.log')
	def myfunc2():
	    pass
	
	myfunc2()
	# Output: myfunc2 was called
	# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建 logit
	class logit(object):
		_logfile = 
		def __init__(self,func):
		def __call__(self, *args):
				return self.func(*args)
		def notify(self):
			# logit
			pass
	
使用
	
	logit.__logfile = 'out2.log'
	@logit
	def myfunc1():
		pass

给logit创建子类，来添加email的功能

	class email_logit(logit):
		def init(self, email='admin@myproject.com', *args, 				**kwargs)
			self.email = email
			super(email_logit, self).__init__(*ARGS, **kwargs)

		def notify(self):
			pass
	
## Global
	
global 变量意味着我们可以在函数以外的区域都能访问这个变量。或返回多个return值


## Mutable
	def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
	
## Slots
	__slots__ = ['name', 'identifier']
第二段代码会为你的内存减轻负担。通过这个技巧，有些人已经看到内存占用率几乎40%~50%的减少

[使用IPython管理内存](https://github.com/ianozsvald/ipython_memory_usage)

## defaultdict
	
	favourite_colours = defaultdict(list)
	# defaultdict(<type 'list'>,
	#    {'Arham': ['Green'],
	#     'Yasoob': ['Yellow', 'Red'],
	#     'Ahmed': ['Silver'],
	#     'Ali': ['Blue', 'Black']
	# })

	import collections
	tree = lambda: collections.defaultdict(tree)
	some_dict = tree()
	some_dict['colours']['favourite'] = "yellow"

	import json
	json.dumps(some_dict)

	## 输出: {"colours": {"favourite": "yellow"}}

## counter
	favs = Counter(name for name, colour in colours)

## Deque

## Namedtuple
namedtuple 的每个实例没有对象字典

	Animal = namedtuple('Animal', 'name, age, type')
	perry = Animal(name='Perry', age=31, type='cat')
	perry[0]   # output : Perry
	perry.name # output : Perry

## Enum
	from collections import namedtuple
	from enum import Enum

	class Species(Enum):
	    cat = 1
	    dog = 2
	    horse = 3
	    aardvark = 4
	    butterfly = 5
	    owl = 6
		platypus = 7
		dragon = 8
		unicorn = 9
	perry = Animal(name='Perry', age=31, type=Species.cat)

以下方法都可以获取到 cat 的值

	Species(1)
	Species['cat']
	Species.cat

## Enumerate
枚举（enumerate）是 Python 内置函数,它允许我们遍历数据并自动计数

	mylist = ['apple', 'banana', 'grapes', pear']
	couter_list = list(enumerate(mylist, 1))
	print(counter_list)   
	# output:
	[(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]

## Dir
如果我们运行 dir() 而不传入参数，那么它会返回当前作用域的所有名字

## Type and id

## Inspect 模块
inspect 模块也提供了许多有用的函数，来获取活跃对象的信息
	import inspect
	inspect.getmembers(str)

# Comprehension
共有三种推导，在Python 2和3中都有支持
- 列表推导
- 字典推导
- 集合推导

	multiples = [i for i in range(30) if i % 3 is 0]
	print(multiples)
	# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

	squared = [x**2 for x in range(10)]

### dict
	mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

	mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

快速对换一个字典的键和值
	{V : k for k, v in dict.items()}

### 集合

	squared = {x**2 for x in [1, 1, 2]}
	print(squared)
	# Output: {1, 4}

## Exception
	
异常处理是一种艺术，一旦你掌握，会授予你无穷的力量
	try:
    	file = open('test.txt', 'rb')
	except IOError as e:
    	print('An IOError occurred. {}'.format(e.args[-1]))


使用三种方法来处理多个异常

	try:
	    file = open('test.txt', 'rb')
	except (IOError, EOFError) as e:
	    print("An error occurred. {}".format(e.args[-1]))
第二种

	try:
    	file = open('test.txt', 'rb')
	except EOFError as e:
   		print("An EOF error occurred.")
    	raise e		
	except IOError as e:
   		print("An error occurred.")
    	raise e

最后一种方式会捕获所有异常	

	try:
   	 file = open('test.txt', 'rb')
	except Exception:
    	# 打印一些异常日志，如果你想要的话
    	raise

else 从句只会在没有异常的情况下执行，而且它会在 finally 语句之前执行

## Class
类是 Python 的核心。它们给了我们很大的力量，但很容易滥用这种力量

- 实例变量用于每个对象都是唯一的数据
- 类变量用于在类的不同实例之间共享的数据
-

	class Cal(object):
		# pi 是类变量
		pi = 3.142
		
		def __init__(self, radius):
			# self.radius 是实例变量
			self.radius = radius
		
		def area(self):
			return self.pi * (self.radius ** 2)

使用不可变类变量时没有太多问题
	
	class SuperClass(object):
	    superpowers = []
	
	    def __init__(self, name):
	        self.name = name
	
	    def add_superpower(self, power):
	        self.superpowers.append(power)

	foo = SuperClass('foo')
	bar = SuperClass('bar')
	foo.name
	# Output: 'foo'
	
	bar.name
	# Output: 'bar'
	
	foo.add_superpower('fly')
	bar.superpowers
	# Output: ['fly']
	
	foo.superpowers
	# Output: ['fly']

为了使你的代码安全抵御这种意外攻击，请确保你不使用可变类变量。 只有当你知道自己在做什么时，才可以使用它们。

## 新的样式类

Python 2.1 中引入了新的样式类，但是现在很多人都不知道它们！之所以如此，是因为 Python 还支持 旧样式类以保持向后兼容性。

	class OldClass():
		def __init__(self):
			print('I am an old class')

	class NewClass(object):
		def __init__(self):
			print('I'm a jazzy new class')
	old = OldClass()

	new = NewClass()


从 object 继承允许新样式类利用一些 魔法。 一个主要优点是您可以使用一些有用的优化，如 __slots__。 您可以使用 super() 和描述符等。

注意：Python 3 只有新式的类。无论您是否从 object 继承，都无关紧要。但是，建议您仍然从 object 继承。

## Magic method
### __init__
### __getitem__
在类中实现 getitem 允许其实例使用 []（索引器）运算符。
	def __getitem__(self,i):

## Lambda
  
	add = lambda x, y: x + y

    print(add(3, 5))

还有一些lambda表达式的应用案例，可以在一些特殊情况下使用

	a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])


## zip
Another way to think of zip() is that it turns rows into columns, and columns into rows. This is similar to transposing a matrix.

zip() in conjunction with the * operator can be used to unzip a list:

# Cache
函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。在 Python 3.2 版本以前我们只有写一个自定义的实现。在 Python 3.2 以后版本，有个 lru_cache 的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。
    from functools import lru_cache

	@lru_cache(maxsize=32)
	def square(x):
		print('computing')
		return x * x


# Python docs
## Performance Measurement

# Anthony explains
## ep487
	
	class C:
		def f(self):
			return 1
		
		def g(self):
			return 2

	def test_f():
		c = C()
		assert c.f() == 1

	def test_g():
		c = C()
		assert c.g() == 2

@pytest.fixture


# Coroutine

	def countdow(n):
		print('Counting down {n}')
		while n > 0:
			yield n	
			n -= 1

Remembering to call .next() is easy to forget	
	
	def coroutine(func):
		def start(*args, **kwargs):
			cr = func(*args, **kwargs)
			cr.next()
			return cr
		return start

	@coroutine
	def grep(pattern):
		print 'Looking for %s' % pattern
		while True:
			line = (yield)
			if pattern in line:
				print(line)


Use .close() to shut it down

Note: Garbage collection also calls close()
Exceptions can be thrown inside a coroutine

	a.throw(RutimeError, 'you are hosed')

Generators produce values
Coroutines tend to consume values
Coroutines are not related to iteration
		
## Pipeline Sources
### The pipeline needs an initial source (a producer)
### The source drives the entire pipeline
	
	def source(target):
		while not donw:
			item = produce_an_item()
			...
			targte.send(item)
			...
		target.close()

### It is typically not a coroutine

## Pipeline Sinks
- The pipeline have an end_point
- Collects all data sent to it an processes it

	@coroutine
	def sink():
		try:
			while True:
				item = (yield)	
				...
			except GeneratorExit:
				# Done
				...

## Pipeline Filters

	@coroutine
	def filter(target):
		while True:
			item = (yield)
			# Transform/filter item
			...
			# Send it along to the next stage
			target.send(item)

# Broadcast

With coroutines, you can send data to multiple
destinations## Coroutines vs. Objects	class GrepHandler(object):
    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target
    def send(self, line):
        if self.pattern in line:
            self.target.send(line)


	@coroutine
	def null():
		while True: item = (yield)


	@coroutine
	def grep(pattern):
		while True:
			line = (yield)
			if pattern in line:
				target.send(d)

			
	line = 'python is nice'
	p1 = grep('python',null()) # Coroutine
	p2 = GrepHandler('python',null()) # Object

	timeit("p1.send(line)","from __main__ import line,p1",number=1000000)
	timeit("p2.send(line)","from __main__ import line,p2",number=1000000)

# Event Handling

## Minimal SAX Example 
	import xml.sax

	class MyHandler(xml.sax.ContentHandler):
		def startElement(self, name, attrs):
			print "startElement", name
		def endElement(self)
			print "endElement",name
		def characters(self,text):
			print "characters', repr(text)[:40]

	xml.sax.parse('somefile.xml', MyHandler())

## State Machines
- State A: Looking for a bus
- State B: Collecting bus attributes
## You can even drop send() operations into C 		PyObject *	py_parse(PyObject *self, PyObject *args) {		PyObject *filename;		PyObject *target;		PyObject *send_method;		if (!PyArgs(args, "sO", &filename, &target)) {			return NULL;		}		send_method = PyObject_GetAttrString(target, "send");		...		/* Invoke target.send(item) */		args = Py_BuildValue("(o)", item);		result = PyEval_CallObject(send_meth, args);		... ## Can also bridge two corutines over a file/pipe- With coroutines, you can separate the
implementation of a task from its execution
environment

You need to carefully study the problem to
know if any of this is a good idea
You also can't create loops or cycles
send() doesn't suspend coroutine execution

# Part 5
## The Task Concept
## Are Coroutines Tasks

# Part 6
# Program Exection
# The Multitasking Problem
# Oerating Systems
# Interrupts and TRaps
# Traps and Ssstem Calls
# Task Switching
# Task Scheduling
# An insight

# Part 7
## Our Challenge
# Some Motivation
# Step 1: Define Tasks
- A task object
	class Task(object):
		taskid = 0
		def __init__(self, target):
			Task.taskid += 1
			self.tid = Task.taskid
			self.target = target
			self.sendval = none
		def run(self):
			self.target.send(self.sendval)

- A task is a wrapper around a coroutine
- There is only one operation: run()

# Step2: The Scheduler

# First Multitasking
- Two tasks
- Runing them into the scheduler
-  
- 
# First Multitasking
- EXAmple ouput
- Emphasize
- Each task run until it hits the yield
- At this point, the scheduler regains control
# The scheduler crashes if a task returnd
# Step 3: TAsk Exit
del self.taskmap[task.tid]# SEcond Multitasking- Two tasks:
- # System Calls	class SystemCall(object):		def handle(self):			pass	class GetTid(SystemCall):		def handle(self):			self.task.sendval = self.task.tid			self.sched.schedule(self.task)	class NewTask(System):		def __init__(self, target):			self.target = target		def handle(self):			self.task# Step 4: System Calls# A first System Call	class GetTid(SystemCall):		def handle(self):			self.task.sendval = self.task.tid			self.sched.schedule(self.task)1. Return a task's ID number
2. The operation is little subtle
3. The sendval attibute is like a return value from system call. it's value is sent into the task when it runs again
# Example of using a system call# Step 5 Task management1. Create a new task
2. Kill an existing task
3. Wait for a task to exit
# Killing Tasks	class KillTask(SysemCall):		def __init__(self, tid):			self.tid = tid		def handle(self):			task = self.sched.taskmap.get(self.tid, None)			if task:				task.target.close()				self.task.sendval = True			else:				self.task.sendval = False			self.sched.schedule(self.task)# Waiting for Tasks- This is a more tricky problem...
- The task that waits has to remove itself from the run queue--it sleeps until child exits
- This require some scheduler changes
# Task Waiting	class Scheduler(object):		def __init__(self):			...			self.exit_waiting = {}			...		def exit(self, task):			print "Task %d terminated" % task.id			del self.taskmap{task.id]			# Notify other tasks waiting for exit			for task in self.exit_waiting.pop(task.tid, []):				self.schedule(task)		def waitforexit(self, task, waitid):			if waittid in self.taskmap:				self.exit_waiting.setdefault(waittid, []).append(task)				return True			else:				return False# Task Waiting	class WaitTask(SystemCall):		def __init__(self, tid):			self.tid = tid		def handle(self):			result = self.sched.waitforexit(self.task, self.tid)			self.task.sendval = result			# If waiting for a non-existense task,			# return immediately without waiting			if not result				self.sched.schedule(self.task)# An Echo Server Attempt## Socket		from socket import socket, AF_INET, SOCKSTREAM)	def server(port):		sock = socket.socket(AF_INET, SOCKSTREAM)		sock.bind(('', port))		sock.listen(5)		while True:			client, addr = sock.accept()			yield NewTask(handle_client(client, addr))	def handle_client(client, addr):		print "Connecting from" , addr		while True:			data = client.recv(65536)			if not data:				break			client.send(data)		client.close()		print "Client closed"		yield	# Make the function a generator/coroutine## Blocking Operation## Non-blocking I/O	reading = [] # List of sockets waiting for read	writing = [] # List of sockets waiting for write		# Poll for activity	r, w, e = select.select(reading, writing, [], timeout)	# r is list of sockets with incoming data	# w is list of sockets ready to accept outgoing data	# e is list of sockets with an error state## Step 6: I/O Waiting	self.read_waiting = {}	self.write_waiting = {}		def waitforread(self, task, fd):		self.read_waiting[fd] = task	def waitforwrite(self, task, fd):		self.write_waiting(fd) = task	def iopoll(self, timeout):		if self.read_waiting or self.write_waiting:			r, w, e = select.select(self.read_waiting, self.write_waiting, [], timeeout)			for fd in r: 				self.sched.schedule(self.read_watinng.pop(fd)			for fd in w:				self.sched.schedule(self.write_waiting.pop(fd))		
- When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.	## When to Poll?	self.iopoll(0)	
- Problem: This might cause excessive polling## A Polling Task	 # A Polling Task	def iotask(self):		while True:			if self.ready.empty():				self.iopoll(None)			else:				self.iopoll(0)			yield	def mainloop(self):		self.new(self.iotask())		# Launch I/O polls		while self.taskmap:			task = self.ready.get()# Read/Write Syscalls1. Two new system calls
	
		class ReadWait(SystemCall):
			def __init__(self, f):
				self.f = f
			def handle(self):
				fd = self.f.fileno()
				self.sched.waitforread(self.task.fd)
	
		class WriteWait(SystemCall):
			def __init__(self.f):
				self.f = f
			def handle(self):
				fd = self.f.fileno()
				self.sched.waitforwrite(self.task, fd)
	

2. These merely wait for I/O events, but do not actually perform I/O

# A New Echo Server
	def handle_client(client, addr):
		print "Conection from", addr
		while True:
			yield ReadWrite(client)
			data = client.recv(65536)
			if not data:
				break
			yield WriteWait(client)
			client.send(data)
		client.close()
		print "client closed"

	def server(port):
		print "Server starting"
		sock = socket(AF_INET, SOCK_STREAM)
		sock.bind(("", port))
		sock.listen(5)
		while True:
			yield ReadWait(sock)
			client, addr = sock.accept()
			yield NewTask(handle_client(client, addr))
	

# The Problem with the Stack

## A Limitation

	def Accept(sock):
		yield ReadWait(sock)
		return sock.accept()

	def server(port):
		...
		while True:
			client, addr = Accept(sock)
			yield NewTask(handle_client(client, addr))
	
## A Problem
	def bar():
		yield

	def foo():
		bar()
## A solution


## Coroutine Trampolining
	# a subroutine
	def add(x, y):
		yield x + y

	# A function that calls a subroutine
	def main():
		r = yield add(1, 2)
		print r
		yield
	# here is very simpler scheduler code
	def run():
		m = main()
		# An example of a "trampoline"
		sub = m.send(None)
		result = sub.send(None)
		m.send(result)

# An Implementation
	class TASK(object):
		def __init__(self, target):
			...
			self.stack = []
		def run(self):
			while True:
				try:
					result = self.target.send(self.sendval)
					if isinstance(result, SystemCall)
						return result
					if isinstance(result, types.Generator)
						self.stack.append(self.target)
						self.sendval = None
						self.target = result
					else:
						if not stack: return
						self.target = self.stack.pop()
						self.sendval = result
				except StopIteration:
					if not self.stack: raise
					self.target = self.stack.pop()
					self.sendval = None				
			

# Some Subroutine

- Blocking I/O can be put inside library fuctions
- These hide all of the low-level details

# A Better Echo Server

# Some Comments


- This is insane
- You now have two types of callables
- For the latter, you always have to yield for both caling and returning values
- The code looks really weirld at first glance
# Coroutines and Methods
- You can take this further and implemnts wrapper object with non-blocking I/O
# A final Echo Server
