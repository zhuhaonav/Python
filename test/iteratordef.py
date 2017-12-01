#迭代器 iter() ,next()
list=[1,2,3,4]
it = iter(list)
for x in it:
  print(x,end=',')

import sys

def fibonacci(n):
  a,b,c=0,1,0
  while True:
    if(c>n):
      return
    yield a
    a,b=b,a+b
    c+=1
f=fibonacci(10)
while True:
  try:
    print (next(f),end=',')
  except StopIteration:

##函数
##匿名函数lambda
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#sum = lambda arg1,arg2:arg1+arg2

#变量的作用域
    total=0
    def sum(arg1,arg2):
      total = arg1 + arg2
      print('局部变量：',total)
      return total
    sum(10,20)
    print ('全局变量：',total)

    num = 1
    def fun1():
      global num #声明
      print(num)
      num = 123
      print(num)
    fun1()

    def outer():
      num = 10
      def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
      inner()
      print(num)
    outer()
      
    sys.exit()