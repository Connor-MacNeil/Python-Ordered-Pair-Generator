from simpleeval import simple_eval


vals1 = [] #? Enter a list of values of x
vals2 = [] #? init for looping

def doRng(minimum,maximum):
    #*ENTER RANGE (MIN,MAX+1)
    for n in range(minimum,maximum):
        vals2.append(n)
    return vals2

#* Define function-----------------------------------------------------------------------------------------------------------------------
def f(x):
    return (-2*(x**2)-5) #?<-----enter question here

#* Define function-----------------------------------------------------------------------------------------------------------------------


def do(v=vals1):
    print("\n")
    for n in v:
        print(f"({n}, {f(n)})")
    print("\n")

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
                do(vals1) 
            elif (ans == "range"):
                try:
                    minimum = int(input("Enter a minimum x value: "))
                    maximum = int(input("Enter a MAXIMUM x value: "))
                except: 
                    print("oops... \n\n\n\n")
                    
                doRng(minimum,maximum)
                do(vals2)
            else:
                print("kthxbai")
                asking = False
        except:
            print("oops\n\n\n")
    print("\n"*80)
mathHelper9000()