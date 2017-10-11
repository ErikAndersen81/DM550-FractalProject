fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
def flatten(fractal): 
    x=str(fractal)
    newfractal=x.replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
    print(newfractal)   
flatten(fractal)
