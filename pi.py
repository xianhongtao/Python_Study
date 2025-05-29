import turtle
import random
import math

# 初始化设置
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("蒙特卡洛法计算圆周率")
screen.tracer(0, 0)  # 禁用自动刷新，手动控制

# 绘制参考图形
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# 绘制正方形
pen.goto(-200, -200)
pen.pendown()
for _ in range(4):
    pen.forward(400)
    pen.left(90)
pen.penup()

# 绘制内切圆
pen.goto(0, -200)
pen.pendown()
pen.circle(200)
pen.penup()

# 状态显示
status = turtle.Turtle()
status.hideturtle()
status.penup()
status.goto(0, 250)

# 初始化计数器
points_inside = 0
total_points = 0
pi_estimate = 0


# 点绘制函数
def draw_point(x, y, color):
    point = turtle.Turtle()
    point.hideturtle()
    point.penup()
    point.goto(x, y)
    point.dot(3, color)


# 主循环
while True:
    # 生成随机点（范围：-200 到 200）
    x = random.uniform(-200, 200)
    y = random.uniform(-200, 200)

    # 判断是否在圆内
    distance = math.sqrt(x**2 + y**2)
    color = "green" if distance <= 200 else "red"

    # 更新计数器
    if distance <= 200:
        points_inside += 1
    total_points += 1

    # 计算π值
    if total_points > 0:
        pi_estimate = 4 * points_inside / total_points

    # 绘制点
    draw_point(x, y, color)

    # 更新状态
    status.clear()
    status.write(
        f"当前点数: {total_points}\n估算π值: {pi_estimate:.10f}",
        align="center",
        font=("Arial", 16, "bold"),
    )

    # 每100个点刷新一次屏幕
    if total_points % 100 == 0:
        screen.update()

# 保持窗口打开（实际不会执行到这里）
turtle.done()
