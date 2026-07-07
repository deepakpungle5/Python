# write a program which accept one number from user and return its factorial.

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact

def main():
    no = int(input("Enter a number : "))
    ret = fact(no)

    print(f"Factorial of {no} is {ret}")

if __name__ == "__main__":
    main()