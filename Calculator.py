#calculator to perform basic arithmetic operations 

def add():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    sum=num1+num2
    print("Addition of two numbers is ",sum)

def sub():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    diff=num1-num2
    print("Subraction of two numbers is ",diff)

def mul():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    multiplication=num1*num2
    print("Multiplication of two numbers is ",multiplication)

def div():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    division=num1/num2
    print("Division of two numbers is ",division)

menu=""" 
           1)add
           2)sub
           3)mul
           4)div
"""
print(menu)
choice=int(input("Enter your choice: "))

if choice==1:
    add()
elif choice==2:
    sub()
elif choice==3:
    mul()
elif choice==4:
    div()
else:
    print("Enter valid choice")                



