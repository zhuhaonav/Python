#类和对象
class MyClass:
  #一个简单实例
  i=12345
  def f(self):
    return 'hello world'
#实例化类
x=MyClass()
#访问类的属性和方法
print('MyClass 类的属性 i 为：',x.i)
print('MyClass 类的方法 f 输出为：',x.f())

#类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
class Complex:
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r,x.i)

#类定义
class people:
  #定义基本属性
  name=''
  age=0
  #定义私有属性
  __weight=0
  #定义构造方法
  def __init__(self, n, a, w):
    self.name=n
    self.age=a
    self.__weight=w
  def speak(self):
    print('%s 说：我 %d 岁。' %(self.name,self.age))
p=people('runoob',10,30)
p.speak()
print(p.age)

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
s = student('ken',10,60,3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")
test.speak()#方法名同，默认调用的是在括号中排前地父类的方法

#父类方法重写
class Parent:
  def myMethod(self):
    print('调用父类方法')

class Child:
  def myMethod(self):
    print('调用子类方法')

c=Child()
c.myMethod()

#两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
#print (counter.__secretCount)  # 报错，实例不能访问私有变量

#运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)