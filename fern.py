import turtle

def stem(t, length, width, segments, curve, steps):
    if steps ==0:
        return
    for i in range(segments):
        t.pensize(width)
        t.lt(curve)
        t.fd(length)
        a=t.clone()
        a.rt(90)
        stem(a, length*0.3, width*0.3, segments, curve, steps-1)
        b=t.clone()
        b.lt(90)
        stem(b, length*0.3, width*0.3, segments, curve, steps-1)
        width *= 0.87
        length *= 0.87
    
        

def main():
    t=turtle.Turtle()
    t.ht()
    t.up()
    t.goto((-200,-100))
    t.down()
    t.speed(0)
    #Ste,(t, length, width, segments, curve, steps)
    stem(t,100,10, 20, 3, 4) # notice curvature of 3 degrees instead of 4.
    turtle.update()
if __name__=="__main__":
    main()
