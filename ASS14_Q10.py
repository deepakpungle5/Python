# Write a lambda function which accept Three number and returns Largest No

LargestNo = lambda no1, no2, no3 : no1 if(no1>no2 and no1>no3) else no2 if (no2>no1 and no2 > no3) else no3

def main ():
    a = int(input("Enter First number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))

    ret = LargestNo(a, b, c)

    print("Largest Number From Given Number is : ",ret)


if __name__ == "__main__":
    main()