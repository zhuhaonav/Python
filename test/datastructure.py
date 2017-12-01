#Python数据结构
##列表推导式
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
del a[:]
print(a)