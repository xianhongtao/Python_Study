print("原票价是: 256")
age = int(input("输入你的年龄: "))
price = 256
if age >= 70:
    price *= 0
elif age >= 60:
    price *= 0.8
elif age >= 18:
    price *= 1
elif age >= 14:
    price *= 0.6
elif age >= 12:
    price *= 0.5
else:
    price *= 0.1
print("你的票价是: ", price)