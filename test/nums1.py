#求100-200之间的质数
from math import sqrt
h=0 
leap=1
list1=[]
for m in range(101,201):
    k = int(sqrt(m+1))
    for i in range(2,k+1):
        if m%i==0:
            leap=0
            break
    if leap==1:
        h += 1
        list1.append(m)    
    leap=1
print('质数：',list1)

#水仙花数
list2=[]
for nums in range(100,1000):
    b = nums // 100
    s = (nums-b*100) // 10 
    g = nums - b*100 -s*10
    if nums == b**3 + s**3 + g**3:
        list2.append(nums)
print('水仙花数：',list2)
