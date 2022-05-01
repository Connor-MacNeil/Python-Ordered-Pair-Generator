from sympy import symbols, substitution 


x = symbols('x')
vals1 = [] #? Enter a list of values of x
vals2 = [] #? init for looping

def doRng(minimum,maximum):
    #*ENTER RANGE (MIN,MAX+1)
    for n in range(minimum,maximum):
        vals2.append(n)
    return vals2

def f(x):
    return (-2*(x**2)-5) #?<-----enter question here

# prompt the user for the expression 
# returns valid expression  
def getExpression():
    while(True):
        try:
            exp = str(input("Enter an equation to solve for a single variable (x):\n> "))
            break
        except:
            print("oops... Try again \n")
    return exp

def generateOrderedPairs(v=vals1):
    for n in v:
        print(f"({n}, {(expression)})")
        

def mathHelper9000():
    asking = True
    while (asking):
        try:
            ans = str(input("\nMANUAL x values OR RANGE of x:\n> "))
            if (ans == "manual"):
                try:
                    howMany = int(input("How many x values?: "))
                    for i in range(0,howMany):
                        nval = int(input("Enter an x value: "))
                        vals1.append(nval)
                except: 
                    print("oops... \n\n\n\n")
                print("\n")    
                generateOrderedPairs(vals1) 
                print("\n")
            elif (ans == "range"):
                try:
                    minimum = int(input("Enter a minimum x value: "))
                    maximum = int(input("Enter a MAXIMUM x value: "))
                except: 
                    print("oops... \n\n\n\n")
                    
                doRng(minimum,maximum)
                print("\n")    
                generateOrderedPairs(vals2) 
                print("\n")
            else:
                print("kthxbai")
                asking = False
        except:
            print("oops\n\n\n")
            
    print("\n"*5)
    
expression = getExpression()
mathHelper9000()