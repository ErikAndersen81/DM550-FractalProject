fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
def flatten(fractal):
    x=0
    newfractal=[]
    while x<len(fractal):
        print(fractal[x])
        x+=1
flatten(fractal)