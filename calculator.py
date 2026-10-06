def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def prd(a,b):
    print(a*b)
def div(a,b):
    if(b==0):
        print("Division by zero error")
        return 0
    print(a/b)
while(True):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    c=int(input("Enter your choice:"))
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    if(c==1):
        add(a,b)
    elif(c==2):
        sub(a,b)
    elif(c==3):
        prd(a,b)
    elif(c==4):
        div(a,b)
    elif(c==5):
        print("Exiting..")
        exit(0)
    else:
        print("Invalid choice")
