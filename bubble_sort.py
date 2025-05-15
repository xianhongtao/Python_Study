a = input()
b = input()
c = input()
d = 0
for i in range(2):
    if a < b :
        d = a
        a = b
        b = d
    if b < c :
        d = b
        b = c
        c = d
print(a + b + c)