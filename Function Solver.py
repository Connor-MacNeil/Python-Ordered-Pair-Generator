# list of values of x
xValues = []

# Prompts the user for a minimum and maximum value, 
# returns a list of values within given range
def getRange():
    while(True):
        try:
            minimum = int(input("Enter a minimum x value: "))
            maximum = int(input("Enter a maximum x value: "))
        except: 
            print("Error: Not a valid integer.")
        break
    for n in range(minimum, (maximum)+1):
        xValues.append(n)
    return xValues

# Prompts the user for a number of x values then, what each value is
# Returns the list of values
def getManual():
    try:
        howMany = int(input("How many x values?: "))
        for i in range(0, howMany):
            nval = int(input("Enter an x value: "))
            xValues.append(nval)
    except:
        print("oops... \n\n\n\n")
    return xValues

# Prompt the user for the expression
# Returns valid expression
def getExpression():
    while(True):
        try:
            exp = str(input("Enter an equation to solve for a single variable (x):\n> "))
            break
        except:
            print("oops... Try something like this: '(2 + 4) * x - 8' \n")
    return exp

# Prompt user for type of coordinate generation
# runs the function corresponding to the choice 
# returns the x values list
def getXValues():
    asking = True
    while (asking):
        try:
            print("Enter 'manual' for specific x values \nOR\nEnter 'range' for a range of x values")
            ans = str(input("> "))
            if (ans == "manual"):
                return getManual()
            elif(ans == "range"):
                return getRange()
        except:
            print("error: not a valid choice. - your options are 'manual' or 'range'.")
            
expression = getExpression()
x = getXValues()

# generate the ordered pairs
for x in xValues:
    y = eval(expression)
    print(f"({x}, {y})")