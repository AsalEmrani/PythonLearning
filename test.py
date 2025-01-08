import turtle
import random

# تنظیم صفحه
screen = turtle.Screen()
screen.setup(width=600, height=500)
turtle.speed(10)  

# رسم مربع ها
for i in range(100):
    # دریافت اندازه، موقعیت و زاویه تصادفی
    size = random.randint(10, 100)
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)

    # رفتن به موقعیت و تنظیم جهت به 30 درجه
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(30)

    # رسم مربع با 4 ضلع
    for j in range(4):
        turtle.forward(size)
        turtle.right(90)

# نگه داشتن پنجره باز
turtle.done()
