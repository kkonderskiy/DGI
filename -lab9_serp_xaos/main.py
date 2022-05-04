import turtle
import random
argcx = [0, -400, 400]
argcy = [0, -400, -400]
point = [0, 0]
turtle.speed(0)


while True:
    turtle.penup()
    turtle.dot(4)
    a = random.randint(0, 2)
    point[0] = (point[0] + argcx[a]) / 2
    point[1] = (point[1] + argcy[a]) / 2

    turtle.goto(point[0], point[1])



turtle.exitonclick()