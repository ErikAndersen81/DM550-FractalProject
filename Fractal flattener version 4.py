fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
def flatten(fractal):
    x=str(fractal)
    newfractal=x.replace("[","")
    newfractal=newfractal.replace("]","")
    newfractal=newfractal.replace("'","")
    newfractal=newfractal.replace(" ","")
    newfractal=newfractal.split(",")
    print(newfractal)
    
flatten(fractal)