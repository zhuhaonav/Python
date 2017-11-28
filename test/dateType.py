#列表
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
 
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#删除元素
list = ['Google', 'Runoob', 1997, 2000]
 
print (list)
del list[2]
print ("删除第三个元素 : ", list)

#列表截取
L = ['Google', 'Taobao', 'Runoob']
print(L[1:])

#列表函数
print(len(L))
print(max(L))
print(min(L))

#元组（不允许修改）
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(tup1+tup2)
del tup3 #元组元素无法删除，删除元组后元组不存在

#Python字典（类似于js对象，key:value）
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict['Name'])#字典的取值方法

del dict['Name'] #删除键'Name'
dict.clear()     # 删除字典
del dict         # 删除字典