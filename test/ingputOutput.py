s = 'hello,test'
print(str(s))#返回一个用户易读的表达形式
print(repr(s))#产生一个解释器易读的表达形式
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x)*2 + ',  y 的值为：' + str(y)*2 + '...'
print(s)
#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1, 11):
  #表示第一个参数x的格式。0 代表x,:2d 表示两个宽度的10进制数显示。
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('-3.14'.zfill(5))
print('3.14'.zfill(5))