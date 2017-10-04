import turtle

def lazy_stem(t, length, width, segments, curve, steps):
    if length < 0.1:
        return
    if steps == 0:
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

def stem(t, length, width, segments, curve, steps):
    if length < 0.1:
        return
    if steps == 0:
        return
    for i in range(segments):
        t.pensize(width)
        t.lt(curve)
        t.fd(length)
        traceback=t.pos()
        t.rt(90)
        stem(t, length*0.3, width*0.3, segments, curve, steps-1)
        b=t.clone()
        b.lt(90)
        stem(b, length*0.3, width*0.3, segments, curve, steps-1)
        width *= 0.87
        length *= 0.87

        

def main():
    t=turtle.Turtle()
    t.ht()
    turtle.tracer(1000)
    t.up()
    t.goto((-200,-100))
    t.down()
    #Ste,(t, length, width, segments, curve, steps)
    stem(t,100,10, 12, 3, 5) # notice curvature of 3 degrees instead of 4.
    turtle.update()
if __name__=="__main__":
    main()
