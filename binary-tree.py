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
    a.rt(35)
    t.lt(35)
    binTree(a,size*(2/3),step-1)
    binTree(t,size*(2/3),step-1)

def main():
    bob = turtle.Turtle()
    bob.hideturtle()
    bob.lt(90)
    turtle.tracer(0)
    bob.pencolor("#555555")
    binTree(bob,100,10)
    screendump(bob)
    
def screendump(t):
    """ Saves the canvas of t as a file.
    """
    img=t.getscreen()
    img.getcanvas().postscript(file="bintree.eps")

if __name__=="__main__":
    main()
    
