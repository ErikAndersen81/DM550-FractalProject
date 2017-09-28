import turtle
import tkinter
from math import sqrt, pi

def triangle(my_turtle, center, size, points_up):
    my_turtle.up()
    x=center[0]
    height=sqrt(size**2-(0.5*size)**2)
    if points_up:
        y=center[1]+(2/3)*height
        my_turtle.rt(60)
    else:
        y = center[1]-(2/3)*height
        my_turtle.lt(120)
    my_turtle.goto(x,y)
    my_turtle.down()
    for i in range(3):
        my_turtle.fd(size)
        my_turtle.rt(120)
    t.setheading(0)

def sierpinsky_triangle(my_turtle, center, size, points_up, step):
    triangle(my_turtle, center, size, points_up)
    if step == 0:
        return
    points_up = not points_up
    triangle(my_turtle, center, size*0.5, points_up)
    height=sqrt(size**2-(0.5*size)**2)
    x=center[0];y=center[1]
    list_of_triangle_centers = [(x+size*0.25,y+height*(1/6)),(x-size*0.25,y+height*(1/6)),(x,y-height*(1/3))]
    for tri in list_of_triangle_centers:
        sierpinsky_triangle(my_turtle, tri, size*0.25, points_up,step-1)

t=turtle.Turtle()
turtle.tracer(1)
t.hideturtle()
sierpinsky_triangle(t, (0,0),300, True, 2)

def screendump(t):
    img=t.getscreen()
    img.getcanvas().postscript(file="duck.eps")
