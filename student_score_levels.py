score = int(input("学生成绩="))
match score:
    case _ if 90 <= score <= 100:
        print("A")
    case _ if 80 <= score < 90:
        print("B")
    case _ if 70 <= score < 80:
        print("C")
    case _ if 60 <= score < 70:
        print("D")
    case _ if 0 <= score < 60:
        print("不及格")
    case _:
        print("输入错误")