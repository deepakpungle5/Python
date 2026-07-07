# write a program which contains one lambda function which accept two parameters and return its multiplication.

mul = lambda no1, no2 : no1 * no2

def main():
    n1 = int(input("Enter First Number : "))
    n2 = int(input("Enter Second Number : "))

    ret = mul(n1,n2)

    print(f"Multiplication of {n1} and {n2} is {ret}")

if __name__ == "__main__":
    main()