def flatten(fractal): 
    x=str(fractal)
    newfractal=x.replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
    print(newfractal)   

if __name__=="__main__":
    fractal=[['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F'], 'R', ['F', 'L', 'F', 'R', 'F', 'L', 'F']]
    flatten(fractal)
