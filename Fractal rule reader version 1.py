F="F"
rule=str(input("What is the rule?"))
depth=int(input("How deep should it be?"))
rule2=rule
def FG(F,rule,depth):
    if depth<=0:
        print(rule)
    else:
       while depth>0:
           rule2=rule.replace("F",rule)
           depth=-1
           print(rule2)
FG(F,rule,depth)

