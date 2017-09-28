import turtle
import tkinter
from math import sqrt, pi

def screendump(t):
    """ Saves the canvas of t as a file.
    """
    img=t.getscreen()
    img.getcanvas().postscript(file="duck.eps")

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
    """ An unsuccesful attempt at a more efficient sierpinsky triangle algorithm.
    """
    triangle(my_turtle, center, size, points_up)
    if step == 0:
        return
    points_up = not points_up
    height=sqrt(size**2-(0.5*size)**2)
    x=center[0];y=center[1]
    if points_up:
        list_of_triangle_centers = [(x+size*0.25,y+height*(1/6)),(x-size*0.25,y+height*(1/6)),(x,y-height*(1/3))]
    else:
        list_of_triangle_centers = [(x+size*0.25,y-height*(1/6)),(x-size*0.25,y-height*(1/6)),(x,y+height*(1/3))]
    triangle(my_turtle, center, size*0.5, points_up)
    for tri in list_of_triangle_centers:
        sierpinsky_triangle(my_turtle, tri, size*0.25, points_up,step-1)

def sierpinsky_triangle2(t,size,step):
    """ Draws Sierpinsky's triangle with a given size and number of steps.
    """
    if step == 0:
        return
    for i in range(3):
        draw_triangle(t,size)
        t.fd(size*2)
        t.rt(120)
        sierpinsky_triangle2(t, size/2, step-1)
    

def draw_triangle(t, size):
    """Draw a triangle of specified size. 
    """
    for i in range(3):
        t.fd(size)
        t.rt(120)

if __name__="__main__":
    t=turtle.Turtle()
    turtle.tracer(1)
    t.hideturtle()
    t.speed(0)
    sierpinsky_triangle2(t,100,5)
    """
    sierpinsky_triangle(t, (0,0),300, True, 2)
    screendump(t)
    """
