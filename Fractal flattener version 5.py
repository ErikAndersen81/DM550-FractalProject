fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
def flatten(fractal): #Denne her er vist big O = n*t ish. Den er linær
    x=str(fractal)
    newfractal=x.replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
    print(newfractal)   
flatten(fractal)