#每个模块都有一个__name__属性，当其值是'__main__'时，
# 表明该模块自身在运行，否则是被引入。
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

import sys
print(dir(sys))#可以找到模块内定义的所有名称