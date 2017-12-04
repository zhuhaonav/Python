#Python数据结构
##列表推导式 ...for...in...if
#可以对序列里每一个元素逐个调用某方法
vec = [2,4,6]
vec2 = [3*x for x in vec]
vec3 = [[x,x**2] for x in vec]
vec4 = [[x,x**2] for x in vec if x>=4]
print(vec2,vec3,vec4)

#矩阵*记录一下，不懂
matrix=[
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
]
matrix2 = [[row[i] for row in matrix] for i in range(4)]
matrix3 = []
for i in range(4):
  matrix3.append([row[i] for row in matrix])
print('matrix2',matrix2,'matrix3',matrix3)

#del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
b = a.copy()
del a[:]
print(b,a)

#元组，序列，集合
a = set('abracgh')
b = set('cenmbhg')
print(a,a^b)#集合运算

#字典创建
dict1 = dict([('space',4139),('guido',4127),('jack',4098)])
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict,dict2)
#遍历
for k,v in dict1.items():
  print(v)
#索引遍历(序列，enumerate函数)
for i,v in enumerate(['tic','tac','toe']):
  print(i,v)
#同时遍历两个或多个序列
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
  print('What is your {0}? It is {1}.'.format(q,a,))
#反向遍历
for i in reversed(range(1, 10, 2)):
  print(i,end=',')
for i in sorted(range(1, 10, 2)):
  print(i,end=',')

