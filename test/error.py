# while True:
#   try:
#     x = int(input("Please enter a number: "))
#     break
#   except ValueError:
#     print("Oops!  That was no valid number.  Try again   ")#提示异常

#如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，
# 那么这个异常会在 finally 子句执行后再次被抛出。
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is", result)
  finally:
    print("executing finally clause")
divide(2, 1)
divide("2", "1")
#一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
#关键词with
with open("myfile.txt") as f:
  for line in f:
    print(line, end="")