import math,time

Number = int(input("请输入一个整数："))
IsPrime = True
MaxDivisorDigit = 1

#开始计时
start = time.time()

MaxDivisorDigit = math.ceil(math.sqrt(Number)/10)

if Number <= 1:
    IsPrime = False
if Number % 2 == 0 or Number % 3 == 0 or Number % 5 == 0 or Number % 7 == 0:
    IsPrime = False

for divisor_index in range(1 , MaxDivisorDigit+1):
    if Number % (divisor_index*10+1) == 0 or Number % (divisor_index*10+3) == 0 or Number % (divisor_index*10+7) == 0 or Number % (divisor_index*10+9) == 0:
        IsPrime = False

if Number in (2 , 3 , 5 , 7, 11 , 13 , 17 , 19):
    IsPrime = True

#结束计时
end = time.time()

print(IsPrime)

print("运行时间：",end-start)