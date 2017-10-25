#state=input("Inpute state ") #Gider ikke lige skrive det ind hver gang
#left=input("Rule ") #Gider ikke lige skrive det ind hver gang
#right=input("Replacment list ") #Gider ikke lige skrive det ind hver gang
state=["F","R","F","R","F"]
left="F"
right=["F","L","F","R","F","L","F"]

def apply(left,right,state):
    fractal=[] #laver tom liste
    x=0
    while x<len(state): #stop parameter
        if state[x]==left[::]: #ser om objekt x i state er ens med left(F)
            fractal.append(right[::]) #Hvis ja append sætter den right ind i listen
        else:
            fractal.append(state[x]) #Hvis nej append sætter den det objekt x i state den kigger på
        x+=1 #skal være += og ikke =+ fml
    print(fractal)
apply(left,right,state)
            
    
