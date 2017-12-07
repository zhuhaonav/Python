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
