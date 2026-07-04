# Write a lambda function which accepts two number and returns maximum number.

MaximunNo = lambda no1, no2 : (no1 > no2)

def main():
    a = int(input("Enter First Number : "))
    b = int (input("Enter Second Number : "))

    ret = MaximunNo(a,b)
    if ret == True:
        print("Greater No is : ",a)

    else :
        print("Greater No is : ",b)


if __name__ == "__main__":
    main()
    