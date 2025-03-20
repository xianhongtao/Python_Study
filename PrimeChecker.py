import math,time

Number = int(input("请输入一个整数："))
IsPrime = True
TensPlace = 1

#开始计时
start = time.time()

TensPlace = math.ceil(math.sqrt(Number)/10)

if Number <= 1:
    IsPrime = False
if Number % 2 == 0 or Number % 3 == 0 or Number % 5 == 0 or Number % 7 == 0:
    IsPrime = False

for i in range(1 , TensPlace+1):
    if Number % (i*10+1) == 0 or Number % (i*10+3) == 0 or Number % (i*10+7) == 0 or Number % (i*10+9) == 0:
        IsPrime = False

if Number in (2 , 3 , 5 , 7, 11 , 13 , 17 , 19):
    IsPrime = True

#结束计时
end = time.time()

print(IsPrime)

print("运行时间：",end-start)