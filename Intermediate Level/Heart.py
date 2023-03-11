import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.hideturtle()
t.goto(0,-10)

turtle.pensize(3)
t.color("blue")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-110, 125)
t.pendown()
t.color("white")
t.write("I Love You",font=("consolas",30,"bold"))

turtle.done()