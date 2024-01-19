given = "p ∧ ~ q ∧ q ∧ p"
vals = []
ops = []
            
def Solve(vals, operation):
    if operation[-1] == "~":
        result = negation(vals[-1])
        vals.pop()
        vals.append(result)
    elif(operation[-1] == "∧"):
        result = conjuction(vals[-1], vals[-2])
        vals.pop()
        vals.pop()
        vals.append(result)
    elif(operation[-1] == "V"):      
        result = disjunction(vals[-1], vals[-2])
        vals.pop()
        vals.pop()
        vals.append(result)  
        
def op_precedence(x):
    if x == "~":
        return 5
    elif x == "∧":
        return 4
    elif x == "V":
        return 3

def negation(x):
    return not x

def conjuction(x, y):
    return x and y

def disjunction (x, y):
    return x or y

for i in given:
    if(i == "p"):
        vals.append(True)
    elif(i == "q"):
        vals.append(True)
    elif(i == " "):
        continue
    else:
        if not ops:
            ops.append(i)
        else:
            if op_precedence(i) < op_precedence(ops[-1]):
                while ops and op_precedence(i) < op_precedence(ops[-1]):
                    if(ops[-1] == "~"):
                        vals.append(negation(vals.pop()))
                        ops.pop()
                    elif(ops[-1] == "∧"):
                        vals.append(conjuction(vals.pop(), vals.pop()))
                        ops.pop()
                ops.append(i)
            else:
                ops.append(i)
                
while ops:
    if ops[-1] == "~":
        Solve(vals, ops[-1])
        ops.pop()
    elif ops[-1] == "∧":
        Solve(vals, ops[-1])
        ops.pop()
    elif ops[-1] == "V":
        Solve(vals, ops[-1])
        ops.pop()

        
"""
    p = True
    q = True
"""
print(f"Given: {given}")
print("p is True")
print("q is True")
print(f"Answer {vals}")
        
