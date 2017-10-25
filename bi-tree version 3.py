x=int(input("How deep a tree do you wish for? And pleas make it an whole numbrer. "))


import turtle #importere turtle og laver lige nogle huritge def af de forskellige funktioner.
def f(w):t.fd(w)
def l(y):t.lt(y)
def r(z):t.rt(z)
def b(m):t.bk(m)

turtle.ht() #Gider ikke se start skildpaden.
t=turtle.Turtle()
t.ht() #Gider ikke se på skildpaden.
turtle.tracer(1000) #må godt gå hurtigt når der tegnes.

import math 
ren=0.7 #scale
s=5 #size of tree
len=10*x
x=x+1 #Jeg skal lægge 1 til x før algoritmen tree(len,x) køre, da den første recursion trækker 1 fra. 
def tree(len,x): #Jeg ignorere skalerings og farve til at starte med. 
    if x>1:
        f(len)
        l(35)
        tree(len*ren,x-1)
        r(70)
        tree(len*ren,x-1)
        l(35)
        b(len)
        
if x<0: #For alle værdier under nul.
    print("You need to plant a seed when young for your grandchildren to have a swing.")

if x==0: #For værdien nul. 
    print("A seed in the ground without water is nothing more than a small rock.")

if 12>x>=1: #For alle træer med minimum 1 branches til 6. 
    l(90)
    tree(len,x)

if x>=13: #For alle træer over debth 5.
    a=str(input("A tree to big will tumble in a storm. Lets cap it at 12, okay? Y/N "))
    if a=="Y" or a=="y" or a=="Yes" or a=="YES":
        l(90)
        tree(len,13)
    else:
        print("You asked for it.")
        l(90)
        tree(len,x)

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

