x=(input("Hello World! How deep a tree do you wish for? And pleas make it an whole numbrer or im gonna round it. ")) #Starter lige med at sige hej.
if x.isalpha():
    exit("That is not a number ")
x=int(round(float(x)))

import turtle #importere turtle og laver lige nogle huritge def af de forskellige funktioner.
def f(w):t.fd(w)
def l(y):t.lt(y)
def r(z):t.rt(z)
def b(m):t.bk(m)
turtle.ht() #Gider ikke se start skildpaden.
t=turtle.Turtle()
t.ht() #Gider ikke se på skildpaden.
t.penup() #Flytter lige starten ned så vi får hele træet med.
t.sety(-250)
t.pendown()
turtle.tracer(1000) #må godt gå hurtigt når der tegnes.
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
if 14>x>=1: #For alle træer med minimum 1 branches til 6. 
    l(90)
    tree(len,x)
if x>=14: #For alle træer over debth 5.
    a=str(input("A tree to big will tumble in a storm. Lets cap it at 12, okay? Y/N "))
    if a=="Y" or a=="y" or a=="Yes" or a=="YES":
        l(90)
        tree(len,13)
    else:
        print("You asked for it.")
        l(90)
        tree(len,x)

turtle.update() 
