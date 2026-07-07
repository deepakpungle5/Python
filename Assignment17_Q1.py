from Arithmetic import *

def main():
    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))

    a = Add(no1, no2)
    s = Sub(no1, no2)
    m = Mul(no1, no2)
    d = Div(no1, no2)

    print("Addition = : ",a)
    print("Substraction = : ",s)
    print("Multiplication = : ",m)
    print("Division = : ",d)


if __name__ == "__main__":
    main()