fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
def flatten(fractal):
    x=0
    newfractal=[]
    while x<len(fractal):
        if fractal[x]==1:
            newfractal.append(fractal[x])
            
        else:
            y=0
            while y<len(fractal[x]):
                newfractal.append(fractal[x])
                y+=1
        x+=1
        print(newfractal)
flatten(fractal)
