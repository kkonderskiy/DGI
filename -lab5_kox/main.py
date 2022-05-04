import turtle
axiom = "F++"
axiom_res = ""
rang = 3


translate = {
    "+": "+",
    "-": "-",
    "F": "F-F++F-F",


}
for i in range(rang):
    for check in axiom:
        axiom_res += translate[check]
    axiom = axiom_res
    axiom_res = ""

print(axiom)

turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()
turtle.speed(0)

lenght = 20
for i in axiom:
    if i == "F" or i == "G":
        turtle.forward(lenght)
    elif i == "+":
        turtle.right(60)
    else:
        turtle.left(60)


turtle.exitonclick()