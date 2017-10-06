import turtle

def lazy_stem(t, length, width, segments, curve, steps):
    if steps == 0:
        return
    for i in range(segments):
        t.pensize(width)
        t.lt(curve)
        t.fd(length)
        a=t.clone()
        a.rt(90)
        lazy_stem(a, length*0.3, width*0.3, segments, curve, steps-1)
        b=t.clone()
        b.lt(90)
        lazy_stem(b, length*0.3, width*0.3, segments, curve, steps-1)
        width *= 0.87
        length *= 0.87


def recursive_stem(t, length, width, segments, curve, steps):
    if steps == 0:
        return
    if length < 0.5:
        return
    for i in range(segments):
        t.pensize(width)
        t.lt(curve)
        t.fd(length)
        pos=t.pos()
        head=t.heading()
        t.rt(90)
        recursive_stem(t, length*0.3, width*0.3, segments, curve, steps-1)
        t.up()
        t.goto(pos)
        t.setheading(head)
        t.down()
        t.lt(90)
        recursive_stem(t, length*0.3, width*0.3, segments, curve, steps-1)
        t.up()
        t.goto(pos)
        t.setheading(head)
        t.down()
        width *= 0.87
        length *= 0.87

def main():
    t=turtle.Turtle()
    t.ht()
    turtle.tracer(9000)
    t.up()
    t.goto((-600,-100))
    t.down()
    #Stem(t, length, width, segments, curve, steps)
    recursive_stem(t,200,6, 5, 3, 5) 
    turtle.update()
    
if __name__=="__main__":
    main()
