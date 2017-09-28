import turtle

def binTree(t, size, step):
    t.pensize(step//2)
    if step == 0:
        return
    if step == 1:
        t.pencolor("#00ff00")
        t.pensize(3)
    t.fd(size)
    a=t.clone()
    a.rt(45)
    t.lt(45)
    binTree(a,size*(2/3),step-1)
    binTree(t,size*(2/3),step-1)

bob = turtle.Turtle()
bob.hideturtle()
bob.speed(0)
bob.lt(90)
bob.pencolor("#555555")
binTree(bob,100,10)

def screendump(t):
    """ Saves the canvas of t as a file.
    """
    img=t.getscreen()
    img.getcanvas().postscript(file="duck.eps")

screendump(bob)
