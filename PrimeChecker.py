import math,time

input = int(input("请输入一个整数："))
is_prime = True
max_divisor_digit = 1

#开始计时
start = time.time()

max_divisor_digit = math.ceil(math.sqrt(input)/10)

if input <= 1:
    is_prime = False
if input % 2 == 0 or input % 3 == 0 or input % 5 == 0 or input % 7 == 0:
    is_prime = False

for divisor_index in range(1 , max_divisor_digit+1):
    if input % (divisor_index*10+1) == 0 or input % (divisor_index*10+3) == 0 or input % (divisor_index*10+7) == 0 or input % (divisor_index*10+9) == 0:
        is_prime = False

if input in (2 , 3 , 5 , 7, 11 , 13 , 17 , 19):
    is_prime = True

#结束计时
end = time.time()

print(is_prime)

print("运行时间：",end-start)