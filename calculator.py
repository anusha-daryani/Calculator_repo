def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if (b==0):
        return "ZeroDivisionError"
    return a/b
########################################
while 1:
    print("-----Calculator-----")
    print("Select a number:")   
    print("1. ADD")
    print("2. SUB")
    print("3. MUl")
    print("4. DIV")
    print("5. EXIT")
    ch=int(input("Enter your choice:"))
    if(ch==1):
      a=int(input("Enter number:"))
      b=int(input("Enter number:"))
      print("Result: ",add(a,b))  
    elif(ch==2):
        a=int(input("Enter number:"))
        b=int(input("Enter number:"))
        print("Result: ",sub(a,b))
    elif(ch==3):
        a=int(input("Enter number:"))
        b=int(input("Enter number:"))
        print("Result: ",mul(a,b))
    elif(ch==4):
        a=int(input("Enter number:"))
        b=int(input("Enter number:"))
        print("Result: ",div(a,b))
    elif(ch==5):
        print("END")
        break
    else:
        print("invaild input")