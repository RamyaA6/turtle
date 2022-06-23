import turtle
col =["red","purple","green","Yellow","orange","blue"]
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(50)
for i in range(120):
    t.color(col[i%6])
    t.forward(i*8)
    t.left(150)
    t.width(1)