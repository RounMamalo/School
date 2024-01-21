vals = []
ops = []    
p = ""
q = ""
r = ""
invalidLetter = False
invalidOperation = False

errorHandler = True #temporary
programRunning = True
def validate_expression(lst):
    valid_characters = set(['p', 'q', 'r'])
    valid_operations = set(['~', '(', ')', '&', '*', '>', '='])
    
    for char in lst: 
        if char not in valid_characters and char.isalpha():
            print(f"\nInvalid Character Found in Given {char} \nPlease use only ['p', 'q', 'r']\n")
            return False
        elif char not in valid_operations and not char.isalpha():
            print(f"\nInvalid Symbol Found in Given {char} \nPlease use only ['~', '(', ')', '&', '*', '>', '=']\n")
            return False
        
    open_parentheses = 0
    close_parentheses = 0
    
    for char in lst:
        if char == '(':
            open_parentheses+=1
        elif char == ')':
            close_parentheses+=1
    
    if not open_parentheses == close_parentheses:
        print("Imbalance Parentheses in the Given")
        return False
    
    for i in range(1, len(lst)):
        if lst[i] in valid_characters and lst[i-1] in valid_characters:
            print(f"\nInvalid Sequencing of Expression \n")
            return False
    
    return True

def negation(x):
    return not x

def conjuction(x, y):
    return x and y

def disjunction (x, y):
    return x or y

def implicaton(x,y):
    return not (x == False and y == True)

def biconditional (x,y):
    return x == y

def Calculate(x, vals, ops):
    if(x == "~"):
        vals.append(negation(vals.pop()))
        ops.pop()
    elif(x == "&"):
        vals.append(conjuction(vals.pop(), vals.pop()))
        ops.pop()
    elif(x == "*"):
        vals.append(disjunction(vals.pop(), vals.pop()))
        ops.pop()
    elif(x == ">"):
        vals.append(implicaton(vals.pop(), vals.pop()))
        ops.pop()
    elif(x == "="):
        vals.append(biconditional(vals.pop(), vals.pop()))
        ops.pop()    

def ProcessSolver(p,q,r,var, vals, ops):
    if var == 'p':
        vals.append(p)
    elif var == 'q':
        vals.append(q)
    elif var == 'r':
        vals.append(r)
    elif not ops:
        ops.append(var)       
    else:
        if var == "(":
            ops.append(var)
        elif var == ")":
            while ops[-1] != "(":
                Calculate(ops[-1], vals, ops)    
            if ops[-1] == "(":
                ops.pop() 
        elif op_precedence(var) < op_precedence(ops[-1]):
            while ops and op_precedence(var) < op_precedence(ops[-1]):
                if(ops[-1] == "("):
                    break
                else:
                    Calculate(ops[-1], vals, ops)     
            ops.append(var)
        else:
            ops.append(var)    

def op_precedence(x):
    if x == "(":
        return 6
    elif x == "~":
        return 5
    elif x == "&":
        return 4
    elif x == "*":
        return 3
    elif x == ">":
        return 2
    elif x == "=":
        return 1

def truthTableGenerator(expression):
    variables = []
    ops = []
    vals = []
    values = [True, False]
    results = []
    if "p" in expression:
        variables.append("p")
    if "q" in expression:
        variables.append("q")
    if "r" in expression:
        variables.append("r")
    
    if not "r" in variables:
        print(f"  p   |  q   | {expression} ")
        print("------------------------")
        for i in values:
            for j in values:
                for k in expression.split():
                    ProcessSolver(i,j,None,k,vals,ops)
                while ops:
                    Calculate(ops[-1], vals, ops)
                results.append(vals[-1])
                print(f"{i} | {j} | {vals.pop()}")
        print("")
    else:
        print(f"  p   |  q   |  r   | {expression} ")
        print("------------------------------")
        for i in values:
            for j in values:
                for l in values:
                    for k in expression.split():
                        ProcessSolver(i,j,l,k,vals,ops)
                    while ops:
                        Calculate(ops[-1], vals, ops)
                    results.append(vals[-1])    
                    print("{i} | {j} | {l} | {vals.pop()}")
        print("")
                
    if all(results):
        print("The logical expression is Tautology")
    elif not any(results):
        print("The logical expression is Contradiction")
    else:
        print("The logical expression is Neither Tautology or Contradiction")
    
def showResult(given, vals):
    print(f"\nGiven: {given}")
    print(f"Answer {vals}")

print("\n!LOGIC CALCULATOR!")

while errorHandler: 
    if vals:
        vals.pop()
        
    print(
    """\nOperations:
Negation: ~ 
Conjunction: &
Disjunction: *
Implication: >
Biconditional: =
    """
    )
    #Main Menu of the Program
    print(
    """1. Logical Expression Evaluator Use Case\n2. Truth Table Generator Use Case\n3. Quit
    """
    )
    print("[Press Any Key To Quit]")
    userInput = int(input("Enter Your Choice (1 or 2): "))
    
    if userInput == 1:
        print("\nNOTE [Add spaces in between variables and operators]\n")
        given = input("Input Logical Expression:")
        
        while validate_expression(given.split()) == False:
            print("Add spaces in between variables and operators")
            given = input("Input Logical Expression:")        

        print("Enter initial truth values. T for True, F for False\n")
        if 'p' in given:
            p = input("p: ").upper()
            
            while p not in ['T', 'F']:
                print("Please Enter T or F only")
                p = input("p: ").upper()
            if p == 'T':
                p = True
            else:
                p = False
                    
        if 'q' in given:
            q = input("q: ").upper()
            while q not in ['T', 'F']:
                print("Please Enter T or F only")
                q = input("q: ").upper()
            if q == 'T':
                q = True
            else:
                q = False
                
        if 'r' in given:
            r = input("r: ").upper()
            while r not in ['T', 'F']:
                print("Please Enter T or F only")
                r = input("r: ").upper()
            if r.upper() == 'T':
                r = True
            else:
                r = False
        else: 
            r = None
        
        for i in given.split():
            ProcessSolver(p, q, r, i, vals, ops)
        while ops:
            Calculate(ops[-1], vals, ops)
        showResult(given, vals)
        
    elif userInput == 2:
        print("\nNOTE [Add spaces in between variables and operators]\n")
        given = input("Input Logical Expression: ")
        
        while validate_expression(given.split()) == False:
            print("Add spaces in between variables and operators")
            given = input("Input Logical Expression:")
            
        print("\n")
        truthTableGenerator(given)
    else:
        break
             
print("Program Terminated")