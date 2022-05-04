import turtle
axiom = "FX"
axiomres = ""
rang = 15

translate = {
    "+": "+",
    "-": "-",
    "F": "F",
    "X": "X+YF+",
    "Y": "-FX-Y"

}
for i in range(rang):
    for check in axiom:
        axiomres += translate[check]
    axiom = axiomres
    axiomres = ""

print(axiom)

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed(0)

lenght = 20
cornel = 90
for i in axiom:
    if i == "F":
        turtle.forward(lenght)
    elif i == "+":
        turtle.left(cornel)
    elif i == "-":
        turtle.right(cornel)


turtle.exitonclick()