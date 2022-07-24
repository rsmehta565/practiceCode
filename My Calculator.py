# Program for Calculator
def ShowOption():
    print("1 : Addition")
    print("2 : Subtraction")
    print("3 : Multiplication")
    print("4 : Division")
    print("Choose the option 1,2,3, or 4")
    try:
        usrInput=int(input("enter the number: "))
        return usrInput
    except:
        print("Enter only number")
        return 0
        
        
def Add(a,b):
    c=a+b
    return c
    
def Sub(a,b):
    c=a-b
    return c
    
def Multi(a,b):
    c=a*b
    return c
    
def Divi(a,b):
    c=a/b
    return c    
    
def MyCalculator():    
    op=ShowOption()
    if op<1 or op>4:
        print("Invalid Input please enter valid number")
        return 0
    userInput1=int(input("Enter the first number: "))
    userInput2=int(input("Enter the second number: "))
    
    result = 0
    
    if op==1:
        result=Add(userInput1,userInput2)
        print("Addition =", end = " ")
    elif op==2:
        result=Sub(userInput1,userInput2)
        print("Subtraction =", end = " ")
    elif op==3:
        result=Multi(userInput1,userInput2)
        print("Multiplication =", end = " ")
    elif op==4:
        try:
            result=Divi(userInput1,userInput2)
            print("Division =", end = " ")
        except ZeroDivisionError:
            print("Exception dive by zero")
            
        
    print(result)


while 1 < 2:        
    MyCalculator()        