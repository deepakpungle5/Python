# Write a lambda function which accept two number and returns Addition

Addition = lambda no1, no2 : no1 + no2 

def main ():
    a = int(input("Enter First number : "))
    b = int(input("Enter Second Number : "))

    ret = Addition(a, b)
    print("Addition of Given Number is : ",ret)

if __name__ == "__main__":
    main()