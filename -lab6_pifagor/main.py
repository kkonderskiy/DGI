import turtle
axiom = "0"
axiomres = ""
rang = 4
stc = []
lenght = 20
cornel = 60

translate = {
    "0": "1[-0]+0",
    "1": "11",
    "[": "[",
    "]": "]",
    "-": "-",
    "+": "+",
}
for i in range(rang):
    for check in axiom:
        axiomres += translate[check]
    axiom = axiomres
    axiomres = ""

print(axiom)

turtle.penup()
turtle.setposition(0, -200)
turtle.pendown()
turtle.left(90)
turtle.speed(0)


for i in axiom:

    if i == "0":
        turtle.forward(lenght)
    elif i == "1":
        turtle.forward(lenght)
    elif i == "+":
        turtle.right(cornel)
    elif i == "-":
        turtle.left(cornel)
    elif i == "[":
        stc.append(turtle.xcor())
        stc.append(turtle.ycor())
        stc.append(turtle.heading())
    elif i == "]":
        turtle.penup()
        turtle.setheading(stc.pop())
        turtle.sety(stc.pop())
        turtle.setx(stc.pop())
        turtle.pendown()



turtle.update()
turtle.mainloop()
turtle.exitonclick()