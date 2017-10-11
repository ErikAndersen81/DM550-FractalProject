import turtle

class SmartTurtle(turtle.Turtle):
    """ This smart turtle can be instantiated with a fdl file, which can be interpreted with SmartTurtle's draw method eg.:
    t=SmartTurtle(fdl='my.fdl')
    t.draw()
    """
    def __init__(self, **kwargs):
        """ ### TASK 12 ###
        Loads fdl file and reads its elements into appropriate data structures
        """
        filename=kwargs.pop('fdl')
        f=open(filename,'r')
        self.rule={}
        self.cmd={}
        self.unfolded=''
        for i in f.readlines():
            i=i.strip()
            i=i.split()
            if len(i)==0:
                continue
            if i[0]=='start':
                self.start=''.join(i[1:])
            if i[0]=='rule':
                self.rule[i[1]]=''.join(i[3:])
            if i[0]=='length':
                self.length=float(i[1])
            if i[0]=='depth':
                self.depth=int(i[1])
            if i[0]=='cmd':
                self.cmd[i[1]]=i[2:]
            super().__init__(**kwargs)
            self.ht()
            
    def step(self):
        """ ### TASK 8 ### 
        Step computes the list of commands to be executed according to the depth given by the fdl. To save memory the list is saved as a string, where each command is represented by a letter. 
TODO: 
* Make adjustments to accommodate an arbitrary number of rules instead of just one or two.
* Investigate whether computations can be made with bytes objects instead of unicode strings.
        """
        state=self.start
        rules = list(self.rule.keys())
        rules.sort()
        m=len(rules)
        if m==1:
            for i in range(self.depth):
                state=state.replace(rules[0],self.rule[rules[0]])
        if m==2:
            for i in range(self.depth):
                state=state.replace(rules[0],"temp")
                state=state.replace(rules[1],self.rule[rules[1]])
                state=state.replace("temp",self.rule[rules[0]])
        self.unfolded=state
        # Clean out 'commands' that are not executing a process.
        # Convert command strings to python functions
        # Convert arguments to floats
        for k in list(self.cmd.keys()):
            if self.cmd[k]==['nop']:
                self.unfolded=self.unfolded.replace(k,'')
            else:
                self.cmd[k][0]=eval('self.' + self.cmd[k][0])
                if len(self.cmd[k])>1:
                    self.cmd[k][1]=float(self.cmd[k][1])

    def draw(self):
        """ ### TASK 11 ### 
        Execute the commands in self.unfolded
        """
        if self.unfolded =='':
            self.step()
        for r in self.unfolded:
            cmd = self.cmd[r]
            if len(cmd)==1:
                arg=self.length
            else:
                arg=cmd[1]
            cmd=cmd[0]
            cmd(arg)
    def scale(self,val):
        self.length *= val

if __name__=="__main__":
    fdl_file=input("Enter fdl file:")
    s=SmartTurtle(fdl=fdl_file)
    turtle.tracer(0)
    s.draw()
    turtle.update()
    turtle.mainloop()
