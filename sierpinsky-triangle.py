import turtle
import tkinter
from math import sqrt, pi

def screendump(t):
    """ Saves the canvas of t as a file.
    """
    img=t.getscreen()
    img.getcanvas().postscript(file="duck.eps")

def triangle(my_turtle, center, side_len, height, points_up=False):
    """ Draws a triangle that points either up or down and has a given side length and center.  
    """
    my_turtle.up()
    x=center[0]
    if points_up:
        y=center[1]+(2/3)*height
        my_turtle.rt(60)
    else:
        y = center[1]-(2/3)*height
        my_turtle.lt(120)
    my_turtle.goto(x,y)
    my_turtle.down()
    for i in range(3):
        my_turtle.fd(side_len)
        my_turtle.rt(120)
    t.setheading(0)

def init_sierpinsky_triangle(my_turtle, center, side_len, steps):
    """ This function is called only once, and basically just draws a triangle pointing up
    and afterwards calls sierpinsky_triangle() which then calls itself recursively
    """
    height=sqrt(side_len**2-(side_len/2)**2)
    triangle(my_turtle, center, side_len, height, True)
    sierpinsky_triangle(my_turtle, center, side_len, height, steps-1)
    
def sierpinsky_triangle(my_turtle, center, side_len, height, step):
    """ Draws a triangle pointing down and calls itself three times if step is gt 0.
    """
    triangle(my_turtle, center, side_len/2, height/2)
    if step >0:
        x=center[0];y=center[1]
        triangle_centers = [(x+side_len/4,y-height/6),(x-side_len/4,y-height/6),(x,y+height/3)]
        for c in triangle_centers:
            sierpinsky_triangle(my_turtle, c, side_len/2, height/2, step-1)

if __name__=="__main__":
    t=turtle.Turtle()
    turtle.tracer(1)
    t.hideturtle()
    t.speed(0)
    init_sierpinsky_triangle(t,(0,0),400,6)
