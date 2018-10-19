"""temp = input("请输入一个年份：")
if temp.isdigit():
    year = int(temp)
    if year % 4 == 0:
        print(str(year)+"是一个润年")
    else:
        print(str(year)+"不是一个润年")
else:
    print("请输入一个年份")
"""
import random

Integer = random.randint(1,100)

times = 3

while times:
   temp = input("请输入一个整数：")
   if temp.isdigit():
       num = int(temp)
       if num == Integer:
           print("猜对了")
       elif num < Integer:
           print("猜的数字小了")
           times = times - 1
       else:
           print("猜的数字太大了")
           times = times - 1
   else:
       print("请输入一个整数")
print("你的机会用完了")
