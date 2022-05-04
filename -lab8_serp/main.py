import turtle
axiom = "F-G-G"
axiom_res = ""
rang = 2


translate = {
    "+": "+",
    "-": "-",
    "F": "F-G+F+G-F",
    "G": "GG"

}
for i in range(rang):
    for check in axiom:
        axiom_res += translate[check]
    axiom = axiom_res
    axiom_res = ""

print(axiom)

turtle.penup()
turtle.goto(-200, -160)
turtle.pendown()
turtle.speed(0)

lenght = 20
for i in axiom:
    if i == "F" or i == "G":
        turtle.forward(lenght)
    elif i == "+":
        turtle.right(120)
    else:
        turtle.left(120)


turtle.exitonclick()