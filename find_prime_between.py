import random

vara = random.randint(100, 1000)
varb = random.randint(100, 1000)
if vara > varb:
    vara, varb = varb, vara


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(n):
    next_num = n + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num


minimun_prime = find_next_prime(vara)

print(f"随机数是{vara} 和 {varb}")

if minimun_prime < varb:
    print(f"大于 {vara} 的最小质数是 {minimun_prime}")
else:
    print("没有符合条件的质数")
