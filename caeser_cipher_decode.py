n = int(input("偏移位数："))
m = input("密文：")
for i in range(len(m)):
    if ord(m[i]) >= 65 and ord(m[i]) <= 90:
        print(chr((ord(m[i]) - 65 - n) % 26 + 65), end="")
    elif ord(m[i]) >= 97 and ord(m[i]) <= 122:
        print(chr((ord(m[i]) - 97 - n) % 26 + 97), end="")
    else:
        print(m[i], end="")
print()