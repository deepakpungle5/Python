# write a program which accepts two number and print addition substraction multiplication and division.

def Addition(a,b):
    return a + b

def Substraction(a,b):
    return a - b

def Multiplication(a,b):
    return a * b

def Division(a,b):
    if b == 0:
        return "Divisible By Zero Error"
    return a / b

def main():
    n1 = int(input("Enter first no : "))
    n2 = int(input("Enter Second no : "))

    add = Addition(n1,n2)
    sub = Substraction(n1,n2)
    mul = Multiplication(n1,n2)
    div = Division(n1,n2)

    print("Addition of given no is : ",add)
    print("Substraction is : ",sub)
    print("Multiplication of give no is : ",mul)
    print("Division is : ",div)

if __name__ == "__main__":      
    main()

