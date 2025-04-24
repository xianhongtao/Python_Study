#Dog age calculator
dog_age = int(input())
if dog_age == 1:
    print("你的狗的年龄相当于人类的14岁")
elif dog_age == 2:
    print("你的狗的年龄相当于人类的22岁")
elif dog_age > 2:
    print("你的狗的年龄相当于人类的", 22 + (dog_age - 2) * 5, "岁")