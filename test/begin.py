a,b = 0,1
while b<10:
  print(b,end=',')#end将结果输出到同一行
  a,b = b,a+b

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
 
### 退出提示
# input("点击 enter 键退出")

##Python循环
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site,end=',')

##range函数,三参数为步长
for i in range(0,10,3):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])

##求质数
for n in range(2,10):
  for x in range(2,n):
    if n % x == 0:
      print(n,'不是质数')
      break
  else:
      print(n,'是质数')
        