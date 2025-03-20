import math,time
def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num))):
        if(num%i == 0):
            return False
    return True
num = int(input(":"))
#开始计时
start = time.time()
print(isPrime(num))
#结束计时
end = time.time()
print("运行时间：",end-start)