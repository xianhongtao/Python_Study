import math

Number = int(input("请输入一个整数："))
IsPrime = True
TensPlace = 1
i = 1

TensPlace = math.ceil(math.sqrt(Number)/10)

if Number <= 1:
    IsPrime = False
if Number % 2 == 0:
    IsPrime = False
if Number % 3 == 0:
    IsPrime = False
if Number % 5 == 0:
    IsPrime = False
if Number % 7 == 0:
    IsPrime = False

if Number in (2 , 3 , 5 , 7):
    IsPrime = True

for i in range(1 , TensPlace+1):
    if Number % ((i*10)+1) == 0:
        IsPrime = False
    if Number % ((i*10)+3) == 0:
        IsPrime = False
    if Number % ((i*10)+7) == 0:
        IsPrime = False
    if Number % ((i*10)+9) == 0:
        IsPrime = False

print(IsPrime)