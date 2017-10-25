import turtle #importere turtle og laver lige nogle huritge def af de forskellige funktioner.
def f(w):t.fd(w)
def l(y):t.lt(y)
def r(z):t.rt(z)
def b(m):t.bk(m)
turtle.ht() #Gider ikke se start skildpaden.
t=turtle.Turtle()
t.ht() #Gider ikke se på skildpaden.
turtle.tracer(1000) #må godt gå hurtigt når der tegnes.

x=int(input("How deep a tree do you wish for? And pleas make it an whole numbrer. "))
#len=100

def tree(x,len): #Jeg ignorere skalerings og farve til at starte med.
        len=10*x
        while x>0:
            f(len)
            l(35)
            if x>1:
                x=-1
                tree(x,len)       
            r(70)
            if x>1:
                x=-1
                tree(x,len)
            l(35)
            b(len)
            len=len*0.7
        
if x<0: #For alle værdier under nul.
    print("You need to plant a seed when young for your grandchildren to have a swing.")

if x==0: #For værdien nul. 
    print("A seed in the ground without water is nothing more than a small rock.")

if 6>x>=1: #For alle træer med minimum 1 branches til 6. 
    l(90)
    tree(x,len)

if x>=6: #For alle træer over debth 5.
    a=str(input("A tree to big will tumble in a storm. Lets cap it at 5, okay? Y/N "))
    if a=="Y" or a=="y" or a=="Yes" or a=="YES":
        len=61
        l(90)
        tree(x,len)
    else:
        print("You asked for it.")
        l(90)
        tree(x,len)

turtle.update()    



 
 
# start X
#rule X -> F L D X R X U L B
#length 100
#depth 10
#cmd X nop
#cmd F fd
#cmd B bk
#cmd R rt 70
#cmd L lt 35
#cmd D scale 0.7
#cmd U scale 1.4285714285714286

